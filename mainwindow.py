from tkinter import *
import tkinter.font
'''
I am going to position and keep track of the value by assigning to integer variables, obviously.
The 1st row is A and 3rd row is C. The first column is 1 and the last column in 3.
So the top left column would be A1.
In this file, I will try to solve a 3x3 window.
'''

mainwindow = Tk()

header_font = tkinter.font.Font(size=20, slant="italic", underline=1)
header_label = Label(mainwindow, text="Sliding Puzzle Solver", font=header_font)
#*Because of columnspan issues, adjust this part later.
#header_label.grid(row=0, column=0)

def start():
    try:
        for item in drop_list:
            item.grid_forget()
    except AttributeError:
        pass
    except NameError:
        pass
    global solve_button
    global value_list
    global variable_counter
    global drop_row_counter
    global drop_column_counter
    global variable_list

    variable_counter = 0
    drop_row_counter = 0
    drop_column_counter = 0
    value_list = ['1', '2','3','4','5','6','7','8','OPEN'] 
    variable_list = [A1, A2, A3, B1, B2, B3, C1, C2, C3]
    A1_drop.grid(row=0, column=0, ipadx=10, ipady=10)
    reset_button = Button(mainwindow, text="Reset\nPosition", width=9, height=2, command=start)
    reset_button.grid(row=4, column=0)
    solve_button = Button(mainwindow, text="Solve", width=18, height=2, state=DISABLED)
    solve_button.grid(row=4, column=1, columnspan=2)
    #!I think the variables are being messed up when I cancel them so I have to do something
    #*I also have to make sure the list turns back to normal


def check(whatever):
    global drop_list
    global drop_row_counter
    global drop_column_counter
    global variable_list
    global value_list
    global variable_counter
    global drop_list
    drop_list = [A1_drop,A2_drop, A3_drop, B1_drop, B2_drop, B3_drop, C1_drop, C2_drop, C3_drop]
    drop_list[variable_counter].grid_forget()
    bg="SystemButtonFace"
    if variable_list[variable_counter].get() == "OPEN":
        bg = "white"
    drop_list[variable_counter] = Label(mainwindow, text=variable_list[variable_counter].get(), width=9, height=3, relief=RIDGE, bg=bg)
    drop_list[variable_counter].grid(row=drop_row_counter, column=drop_column_counter)
    value_list.remove(variable_list[variable_counter].get())
    variable_counter += 1
    if drop_column_counter == 2:
        drop_column_counter = 0
        drop_row_counter += 1
    else:
        drop_column_counter += 1
    try:
        variable_list[variable_counter].set(value_list[0])
        drop_list[variable_counter] = OptionMenu(mainwindow, variable_list[variable_counter], *value_list, command=check)
        drop_list[variable_counter].grid(row=drop_row_counter, column=drop_column_counter, ipadx=10, ipady=10, sticky=W)
    except IndexError:
        solve_button.config(state=NORMAL)






A1 = StringVar()
A1.set(value_list[0])
A2 = StringVar()
A3 = StringVar()
B1 = StringVar()
B2 = StringVar()
B3 = StringVar()
C1 = StringVar()
C2 = StringVar()
C3 = StringVar()

start()

#A1_frame = LabelFrame(mainwindow, width=20, height=5)

A1_drop = OptionMenu(mainwindow, A1, *value_list, command=check)
A2_drop = ""
A3_drop = ""
B1_drop = ""
B2_drop = ""
B3_drop = ""
C1_drop = ""
C2_drop = ""
C3_drop = ""
drop_list = [A1_drop,A2_drop, A3_drop, B1_drop, B2_drop, B3_drop, C1_drop, C2_drop, C3_drop]

#A1_frame.grid(row=0, column=0)


mainloop()

