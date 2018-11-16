from tkinter import *


def graphical_grid_init():
    window = Tk()
    label_field = Label(window,text="2048")
    toplevel = Toplevel()

    toplevel.grid()
    label_field.pack()
    window.mainloop()




