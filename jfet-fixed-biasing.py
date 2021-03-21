#using matplotlib, numpy, tkinter
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

#matplotlib setup
plt.style.use('seaborn-whitegrid')
fig = plt.figure()
ax = plt.axes()

#tkinter GUI
master = tk.Tk()
master.title("JFET Fixed Bias Point Calculator")
tk.Label(master, text="Vgg").grid(row=0)
tk.Label(master, text="Vp").grid(row=1)
tk.Label(master, text="idss").grid(row=2)
tk.Label(master, text="V").grid(row=0, column=2)
tk.Label(master, text="V").grid(row=1, column=2)
tk.Label(master, text="mA").grid(row=2, column=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


def fixed_biasing():
    Vgg = float(e1.get())*(-1)
    Vp = float(e2.get())
    idss = float(e3.get())
    idq = round(idss*(1-(Vgg/Vp))**2, 4)
    Vgsq = Vgg
    tk.Label(master, text="idq: " + str(idq) + "mA").grid(row=3,
                                                  column=1,
                                                  )
    tk.Label(master, text="Vgsq: " + str(Vgsq) + "V").grid(row=4,
                                                  column=1,
                                                  )


#plot
def fixed_plot():
    Vgg = float(e1.get())*(-1)
    Vp = float(e2.get())
    idss = float(e3.get())
    x = np.linspace(Vp, 1, 100)
    x_conv = np.asarray(x)/Vp
    y = idss*(1-(x_conv))**2
    idq = idss*(1-(Vgg/Vp))**2
    Vgsq = Vgg
    plt.plot(x, y, '-r', label='Transfer Curve')
    plt.axvline(x=Vgg, color='g', label='Fixed Vgsq')
    plt.plot(Vgsq, idq, 'bo', label='idq Intersection')
    plt.xlabel('Vgs', color='#1C2833')
    plt.ylabel('idq', color='#1C2833')
    plt.legend(loc='upper left')
    plt.show()


tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=5,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)

tk.Button(master,
          text='Solve', command=fixed_biasing).grid(row=5,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.Button(master,
          text='Plot', command=fixed_plot).grid(row=5,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)


master.mainloop()


