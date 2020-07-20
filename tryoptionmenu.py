from tkinter import *
#!I am going to scrap the making dropdown menus because they can be really complicated.
#*Instead, I can make entry boxes for everything and check the values

root = Tk()
black_list =[]

def check(a,b, c, d):

    if checker2.get() in black_list:
        print("lol")
    elif checker1.get() in my_list:
        black_list.append(checker1.get())
        print(black_list)





my_list = ['1','2','3']

checker1 = StringVar()
checker1.trace_add('write', lambda: check("a", "b", "c", checker1))
#*Trace add is not really working the best
checker2=StringVar()
checker2.trace_add('write', lambda: check("a", "b", "c", checker2))

a = Entry(root, textvariable=checker1)
a.grid(row=0, column=0)

b = Entry(root, textvariable=checker2)
b.grid(row=1, column=0)

mainloop()
