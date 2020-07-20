from tkinter import *

root = Tk()

def change(abc):
    global my_list
    global last
    #b.config(values=*(my_list.remove(a.get(
    #!I think I have to keep track of all the indexes and items or at least the mnost recent ones.
    my_list.remove(value1.get())
    b = OptionMenu(root, value2, *my_list)
    b.grid(row=1, column=0)

value1 = StringVar()
value1.set('1')
value2 = StringVar()
value2.set('1')
my_list = ['1','2','3']
a = OptionMenu(root, value1, *my_list, command=change)
a.grid(row=0, column=0)



mainloop()