'''
In this file, I want to make sure the moving of the tiles work properly.
'''
from tkinter import *
import tkinter.font

root = Tk()

my_canvas = Canvas(root, width=300, height=300, bg="white")
my_canvas.grid(row=0, column=0, columnspan=4)

coord_list = [100, 120, 140]

def move_up():
    #*I can get the 0
    go_next = True
    for list_ in row_list:
        print(list_)
        for item in list_:
            if open9 in list_ and list_.index(open9) == 2:
                go_next = False
                break
    #*If not necessary, I will delete this coordinate requirement.
    if not go_next:
        print("cannot run")
    #*I will create an else for this when I finish the other ones.
    else:
        print("can run")

def move_down():
    #*I think I can simplify this forloop process in the future.
    go_next = True
    for list_ in row_list:
        for item in list_:
            if open9 in list_ and list_.index(open9) == 0:
                go_next = False
                break
    if not go_next:
        print("cannot run")
    else:
        print("will run")

def move_left():
    go_next = True
    for list_ in col_list:
        if open9 in list_ and col_list.index(list_) == 2:
            go_next = False
            break
    
    if not go_next:
        print("cannot run")

def move_right():
    pass


my_font = tkinter.font.Font(size=15)
text1 = my_canvas.create_text(100, 100, text="1", font=my_font)
text2 = my_canvas.create_text(120, 100, text="2", font=my_font)
text3 = my_canvas.create_text(140, 100, text="3", font=my_font)
text4 = my_canvas.create_text(100, 120, text="4", font=my_font)
text5 = my_canvas.create_text(120, 120, text="5", font=my_font)
text6 = my_canvas.create_text(140, 120, text="6", font=my_font)
text7 = my_canvas.create_text(100, 140, text="7", font=my_font)
text8 = my_canvas.create_text(120, 140, text="8", font=my_font)
open9 = my_canvas.create_text(140, 140, text="O", font=my_font, fill ="red")

#*Maybe it might be more convenient to put these in a nested list.
row_list = [[text1, text2, text3], [text4, text5, text6], [text7, text8, open9]]
col_list = [[text1, text4, text7], [text2, text5, text8], [text3, text6, open9]]


button_up = Button(root, text="up", command=move_up)
button_up.grid(row=1, column=0)
button_down = Button(root, text="down", command=move_down)
button_down.grid(row=1, column=1)
button_left = Button(root, text="left", command=move_left)
button_left.grid(row=1, column=2)
button_right = Button(root, text="right", command=move_right)
button_right.grid(row=1, column=3)


mainloop()