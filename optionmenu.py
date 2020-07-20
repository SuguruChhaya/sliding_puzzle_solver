'''
I am scraping the config idea cuz it won't work.
The four ideas remaining are...

1. Create new optionmenu based on what was typed previously.
2. Create new entry based on what was typed previously.
3. Have optionmenus with all selection but make it able to check whether option already exists.
4. Use text to check whether option already exists.
'''

#*With a clear mind, I am going to try option 1
from tkinter import *
#*Works pretty well!!
root = Tk()
'''
def check(whatever):
    global a
    a.grid_forget()
    a = Label(root, text=abc.get())
    a.grid(row=0, column=0)
    my_list.remove(abc.get())
    abc.set(my_list[0])
    b = OptionMenu(root, abc, *my_list)
    b.grid(row=1, column=0)


my_list = ['1', '2','3']
abc = StringVar()
abc.set(my_list[0])

a = OptionMenu(root, abc, *my_list, command=check)
a.grid(row=0, column=0)
'''
#*Since I can't use lambda, I have to manually track which optionmenu was clicked last
#*I will create a version with 3 optionmenus.
def check(next):
    #!To reuse the function, I need to generalize many variables and keep track of them.
    global optionmenu_list
    global optionmenu_counter
    global variable_list
    optionmenu_list[optionmenu_counter].grid_forget()
    optionmenu_list[optionmenu_counter] = Label(root, text=variable_list[optionmenu_counter].get())
    optionmenu_list[optionmenu_counter].grid(row=optionmenu_counter, column=0)
    my_list.remove(variable_list[optionmenu_counter].get())
    optionmenu_counter += 1
    try:
        variable_list[optionmenu_counter].set(my_list[0])
        optionmenu_list[optionmenu_counter] = OptionMenu(root, variable_list[optionmenu_counter], *my_list, command=check)
        optionmenu_list[optionmenu_counter].grid(row=optionmenu_counter, column=0)
    except IndexError:
        pass

my_list = ['1', '2','3']
abc1 = StringVar()
abc1.set(my_list[0])
abc2 = StringVar()
abc3 = StringVar()
#*I think it will be needed to create a variable list
variable_list = [abc1, abc2, abc3]

#?Lambda somehow doesn't work very well...
a = OptionMenu(root, abc1, *my_list, command=check)
#*Rather than making a new variable inside a function, I should try to define them outside as much as possible.
b = ""
c = ""
optionmenu_list = [a, b, c]
optionmenu_counter = 0
a.grid(row=0, column=0)

mainloop()
