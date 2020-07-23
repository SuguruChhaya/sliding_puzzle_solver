from tkinter import *



class SetupWindow():

    def __init__(self, root):
        #*Since I cannot declare string variables before root is passed, I am declaring it inside the __init__ method.
        SetupWindow.dimension = StringVar()
        SetupWindow.dimension.set("3x3")
        SetupWindow.speed = StringVar()
        SetupWindow.speed.set("3sec")
        self.root = root
        self.info_text = "Welcome to number setup window!!\n Select the dimensions and the\n speed of explanation."
        self.info_label = Label(self.root, text=self.info_text)
        self.info_label.grid(row=0, column=0)
        self.dimension_label = Label(self.root, text="Dimensions:")
        self.dimension_label.grid(row=1, column=0)
        #*If I need to access these String variables later, I might have to make them class variables.

        self.dimension_list = ["3x3", "4x4", "5x5"]
        self.dimension_dropdown = OptionMenu(self.root, self.dimension, *self.dimension_list)
        self.dimension_dropdown.grid(row=2, column=0)
        self.speed_label = Label(self.root, text="Speed of explanation\n(Seconds per move):")
        self.speed_label.grid(row=3, column=0)
        self.speed_list = ["1sec", "2sec", "3sec", "4sec", "5sec"]
        self.speed_dropdown = OptionMenu(self.root, self.speed, *self.speed_list)
        self.speed_dropdown.grid(row=4, column=0, ipadx=20, ipady=20)
        self.start_button = Button(self.root, text="Start!!", width=10, height=2, bg="orange", command=self.start)
        self.start_button.grid(row=5, column=0)

    def start(self):
        self.root.destroy()
        #*I am going to add the class call for the mainwindow below.
        mainwindow = Tk()
        mainwindow.title("Main Window")
        a = MainWindow(mainwindow)
        #*The __init__ method is called when a different method in the class is called.
        a.start()


class MainWindow():
    def __init__(self, root):
        self.root = root
        self.variable_counter = 0
        self.drop_row_counter = 0
        self.drop_column_counter = 0
        self.value_list = ['1', '2','3','4','5','6','7','8','OPEN'] 
        MainWindow.A1 = StringVar()
        MainWindow.A1.set(self.value_list[0])
        MainWindow.A2 = StringVar()
        MainWindow.A3 = StringVar()
        MainWindow.B1 = StringVar()
        MainWindow.B2 = StringVar()
        MainWindow.B3 = StringVar()
        MainWindow.C1 = StringVar()
        MainWindow.C2 = StringVar()
        MainWindow.C3 = StringVar()
        self.variable_list = [MainWindow.A1, MainWindow.A2, MainWindow.A3, MainWindow.B1, MainWindow.B2, MainWindow.B3, MainWindow.C1, MainWindow.C2, MainWindow.C3]
        self.A1_drop = OptionMenu(root, MainWindow.A1, *self.value_list, command=self.check)
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
        self.__init__(self.root)


        self.A1_drop.grid(row=0, column=0, ipadx=10, ipady=10)
        self.reset_button = Button(self.root, text="Reset\nPosition", width=9, height=2, command=self.start)
        self.reset_button.grid(row=4, column=0)
        self.solve_button = Button(self.root, text="Solve", width=18, height=2, state=DISABLED)
        self.solve_button.grid(row=4, column=1, columnspan=2)

    def check(self, *args):
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
            self.drop_list[self.variable_counter] = OptionMenu(self.root, self.variable_list[self.variable_counter], *self.value_list, command=self.check)
            self.drop_list[self.variable_counter].grid(row=self.drop_row_counter, column=self.drop_column_counter, ipadx=10, ipady=10, sticky=W)
        except IndexError:
            self.solve_button.config(state=NORMAL)




setupwindow = Tk()
setupwindow.title("Setup Window")
a = SetupWindow(setupwindow)

mainloop()