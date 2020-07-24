'''
In this file, I want to make sure the moving of the tiles work properly.
I will want to refactor this cuz I think it can be way shorter.
'''
from tkinter import *
import tkinter.font

root = Tk()

my_canvas = Canvas(root, width=300, height=300, bg="white")
my_canvas.grid(row=0, column=0, columnspan=4)

coord_list = [100, 120, 140]

def move_up():
    global row_list
    global col_list
    #*I can get the 0
    go_next = True
    for sub_row in row_list:
        for item in sub_row:
            if open9 in sub_row and row_list.index(sub_row) == 2:
                go_next = False
                break
            elif item == open9:
                in_row_list = row_list.index(sub_row)
                in_sub_row = sub_row.index(item)
                break

    for sub_col in col_list:
        for item in sub_col:
            if item == open9:
                in_col_list = col_list.index(sub_col)
                in_sub_col = sub_col.index(item)
                break
        
    
    #*If not necessary, I will delete this coordinate requirement.
    if not go_next:
        pass
    #*I will create an else for this when I finish the other ones.
    else:
        my_canvas.move(open9, 0, 20)
        my_canvas.move(row_list[in_row_list + 1][in_sub_row], 0, -20)
        #!Careful with mutation
        mut1 = row_list[in_row_list][in_sub_row]
        mut2 = row_list[in_row_list + 1][in_sub_row]
        row_list[in_row_list][in_sub_row] = mut2
        row_list[in_row_list + 1][in_sub_row] = mut1
        mut3 = col_list[in_col_list][in_sub_col]
        mut4 = col_list[in_col_list][in_sub_col + 1]
        col_list[in_col_list][in_sub_col] = mut4
        col_list[in_col_list][in_sub_col + 1] = mut3

def move_down():
    #*I think I can simplify this forloop process in the future.
    #*Make range?
    global row_list
    global col_list
    go_next = True
    for sub_row in row_list:
        for item in sub_row:
            if open9 in sub_row and row_list.index(sub_row) == 0:
                go_next = False
                break
            elif item == open9:
                in_row_list = row_list.index(sub_row)
                in_sub_row = sub_row.index(item)
                break

    for sub_col in col_list:
        for item in sub_col:
            if item == open9:
                in_col_list = col_list.index(sub_col)
                in_sub_col = sub_col.index(item)
                break
    if not go_next:
        pass
    else:
        my_canvas.move(open9, 0, -20)
        my_canvas.move(row_list[in_row_list - 1][in_sub_row], 0, 20)
        #!Careful with mutation
        mut1 = row_list[in_row_list][in_sub_row]
        mut2 = row_list[in_row_list - 1][in_sub_row]
        row_list[in_row_list][in_sub_row] = mut2
        row_list[in_row_list - 1][in_sub_row] = mut1
        mut3 = col_list[in_col_list][in_sub_col]
        mut4 = col_list[in_col_list][in_sub_col - 1]
        col_list[in_col_list][in_sub_col] = mut4
        col_list[in_col_list][in_sub_col - 1] = mut3

def move_left():
    global row_list
    global col_list
    go_next = True
    for sub_col in col_list:
        for item in sub_col:
            if open9 in sub_col and col_list.index(sub_col) == 2:
                go_next = False
                break
            elif item == open9:
                in_col_list = col_list.index(sub_col)
                in_sub_col = sub_col.index(item)
                break
        
    for sub_row in row_list:
        for item in sub_row:
            if item ==open9:
                in_row_list = row_list.index(sub_row)
                in_sub_row = sub_row.index(item)
                break
        #*Need to change the list anyways so I think it is ok for diving deeper
    
    if not go_next:
        pass

    else:
        #*Don't know if this will move it right.
        my_canvas.move(open9, 20, 0)
        my_canvas.move(col_list[in_col_list + 1][in_sub_col], -20, 0)
        mut1 = col_list[in_col_list][in_sub_col]
        mut2 = col_list[in_col_list + 1][in_sub_col]
        col_list[in_col_list][in_sub_col] = mut2
        col_list[in_col_list + 1][in_sub_col] = mut1
        mut3 = row_list[in_row_list][in_sub_row]
        mut4 = row_list[in_row_list][in_sub_row + 1]
        row_list[in_row_list][in_sub_row] = mut4
        row_list[in_row_list][in_sub_row + 1] = mut3



def move_right():
    global row_list
    global col_list
    go_next = True
    for sub_col in col_list:
        for item in sub_col:
            if open9 in sub_col and col_list.index(sub_col) == 0:
                go_next = False
                break
            elif item == open9:
                in_col_list = col_list.index(sub_col)
                in_sub_col = sub_col.index(item)
                break
        
    for sub_row in row_list:
        for item in sub_row:
            if item ==open9:
                in_row_list = row_list.index(sub_row)
                in_sub_row = sub_row.index(item)
                break

    if not go_next:
        pass
    else:
        my_canvas.move(open9, -20, 0)
        my_canvas.move(col_list[in_col_list - 1][in_sub_col], 20, 0)
        mut1 = col_list[in_col_list][in_sub_col]
        mut2 = col_list[in_col_list - 1][in_sub_col]
        col_list[in_col_list][in_sub_col] = mut2
        col_list[in_col_list - 1][in_sub_col] = mut1
        mut3 = row_list[in_row_list][in_sub_row]
        mut4 = row_list[in_row_list][in_sub_row - 1]
        row_list[in_row_list][in_sub_row] = mut4
        row_list[in_row_list][in_sub_row - 1] = mut3
    

my_font = tkinter.font.Font(size=15)
text1 = my_canvas.create_text(100, 100, text="1", font=my_font)
text2 = my_canvas.create_text(120, 100, text="2", font=my_font)
text3 = my_canvas.create_text(140, 100, text="3", font=my_font)
text4 = my_canvas.create_text(100, 120, text="4", font=my_font)
text5 = my_canvas.create_text(120, 120, text="5", font=my_font)
text6 = my_canvas.create_text(140, 120, text="6", font=my_font)
text7 = my_canvas.create_text(100, 140, text="7", font=my_font)
text8 = my_canvas.create_text(120, 140, text="8", font=my_font)
open9 = my_canvas.create_text(140, 140, text="", font=my_font, fill ="red")

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