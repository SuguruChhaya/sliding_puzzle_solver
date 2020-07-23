'''
I will try to fix many of the bugs I found in the previous class stuff.
'''
from tkinter import *
import tkinter.font

class MainWindow():
    print("__init__ is ran")
    def __init__(self, root):
        self.root = root
        self.variable_counter = 0
        self.drop_row_counter = 0
        self.drop_column_counter = 0
        self.value_list = ['1', '2','3','4','5','6','7','8','OPEN'] 
        self.A1 = StringVar()
        self.A1.set(self.value_list[0])
        self.A2 = StringVar()
        self.A3 = StringVar()
        self.B1 = StringVar()
        self.B2 = StringVar()
        self.B3 = StringVar()
        self.C1 = StringVar()
        self.C2 = StringVar()
        self.C3 = StringVar()
        self.variable_list = [self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3]
        self.A1_drop = OptionMenu(root, self.A1, *self.value_list, command=self.check)
        self.A2_drop = ""
        self.A3_drop = ""
        self.B1_drop = ""
        self.B2_drop = ""
        self.B3_drop = ""
        self.C1_drop = ""
        self.C2_drop = ""
        self.C3_drop = ""
        self.drop_list = [self.A1_drop,self.A2_drop, self.A3_drop, self.B1_drop, self.B2_drop, self.B3_drop, self.C1_drop, self.C2_drop, self.C3_drop]
        #!Should never include this.
        #self.start()
    def start(self, *args):
        print("start is ran")
        try:
            for item in self.drop_list:
                item.grid_forget()
        except AttributeError:
            pass
        except NameError:
            pass
        #!I have to manually reset the values
        #*self.variable_list reset
        #*I cannot do a manual reset using __init__ as long as __init__ calls start() at the end at line 36
        #?I think I can try combining __init__ and start and see if it is any good.
        #*It worked awesome.
        self.__init__(root)

        for a in self.variable_list:
            print(a.get())
        self.variable_list = [self.A1, self.A2, self.A3, self.B1, self.B2, self.B3, self.C1, self.C2, self.C3]

        self.A1_drop.grid(row=0, column=0, ipadx=10, ipady=10)
        self.reset_button = Button(self.root, text="Reset\nPosition", width=9, height=2, command=lambda: self.start(root))
        self.reset_button.grid(row=4, column=0)
        self.solve_button = Button(self.root, text="Solve", width=18, height=2, state=DISABLED)
        self.solve_button.grid(row=4, column=1, columnspan=2)

    def check(self, *args):
        print("check is ran")
        print(f"self.variable counter: {self.variable_counter}")
        print(f"self.variable_list: ")
        for item in self.variable_list:
            print(item.get())
        print(f"self.drop_list: {self.drop_list}")
        print(f"self.drop_row_counter: {self.drop_row_counter}")
        print(f"self.drop_column_counter: {self.drop_column_counter}")
        self.drop_list[self.variable_counter].grid_forget()
        self.bg="SystemButtonFace"
        if (self.variable_list[self.variable_counter]).get() == "OPEN":
            self.bg = "white"
        #!root is somehow a string!!
        #*root is somehow having the same value as what I selected from the optionmenu!!
        self.drop_list[self.variable_counter] = Label(self.root, text=self.variable_list[self.variable_counter].get(), width=9, height=3, relief=RIDGE, bg=self.bg)
        self.drop_list[self.variable_counter].grid(row=self.drop_row_counter, column=self.drop_column_counter)
        self.value_list.remove(self.variable_list[self.variable_counter].get())
        self.variable_counter += 1
        if self.drop_column_counter == 2:
            self.drop_column_counter = 0
            self.drop_row_counter += 1
        else:
            self.drop_column_counter += 1
        try:
            self.variable_list[self.variable_counter].set(self.value_list[0])
            self.drop_list[self.variable_counter] = OptionMenu(root, self.variable_list[self.variable_counter], *self.value_list, command=self.check)
            self.drop_list[self.variable_counter].grid(row=self.drop_row_counter, column=self.drop_column_counter, ipadx=10, ipady=10, sticky=W)
        except IndexError:
            self.solve_button.config(state=NORMAL)

root = Tk()
a = MainWindow(root)
a.start()


mainloop()
