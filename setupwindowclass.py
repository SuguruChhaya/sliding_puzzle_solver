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
        self.solve_button = Button(self.root, text="Solve", width=18, height=2, state=DISABLED, command=self.goto_solve)
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

    def goto_solve(self):
        a = Solve()
        #*The reason I created a separate function is to add the following line and to make sure __init__ and the other functions are separated.
        a.solve_1()

#*The following class is just for solving the algorithm and doesn't create any graphics.
class Solve():
    def __init__(self):
        #*I can successfully get the values of the class variables.
        self.solve_row = [[MainWindow.A1.get(), MainWindow.A2.get(), MainWindow.A3.get()], 
                        [MainWindow.B1.get(), MainWindow.B2.get(), MainWindow.B3.get()], 
                        [MainWindow.C1.get(), MainWindow.C2.get(), MainWindow.C3.get()]]
        
        self.solve_col = [[MainWindow.A1.get(), MainWindow.B1.get(), MainWindow.C1.get()],
                        [MainWindow.A2.get(), MainWindow.B2.get(), MainWindow.C2.get()],
                        [MainWindow.A3.get(), MainWindow.B3.get(), MainWindow.C3.get()]]

        #*Converting the "OPEN" to '9' for future convenience
        for sub_row in self.solve_row:
            for item in sub_row:
                if item == "OPEN":
                    self.nine_solve_row_index = self.solve_row.index(sub_row)
                    self.nine_sub_row_index = sub_row.index(item)
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = '9'

        for sub_col in self.solve_col:
            for item in sub_col:
                if item == "OPEN":
                    self.nine_solve_col_index = self.solve_col.index(sub_col)
                    self.nine_sub_col_index = sub_col.index(item)
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = '9'

        #*I want to copy this stage of the list as a class variable so I can reuse it when I create the GUI.
        #*I can use the .copy() method to create a new list which doesn't change its value when the original was changed.
        #*But since whenever the __init__ method is ran, the original updates itself, I can make a new method just for copying.
        #*Since this is such a pain and the list inside the tuple just changes, I am going to redo the process again later.

    def solve_1(self):
        #!The following variables keep track of which ways I should not move to.
        check_up_bool = True
        check_down_bool = True
        check_left_bool = True
        check_right_bool = True
        #*I am going to check whether the copy actually worked by changing original
        #*Find the initial location of '1'.
        #*A class variable list to track everything we did. Can be accessed from other classes.
        Solve.instruction_list = []
        #*Create a while loop and include possible strategies.
        while self.solve_row[0][0] != '1':
            for sub_row in self.solve_row:
                for item in sub_row:
                    if item == '1':
                        self.one_solve_row_index = self.solve_row.index(sub_row)
                        self.one_sub_row_index = sub_row.index(item)

            #*I honestly don't know if I am going to need a column explanation but I am just going to add it there.
            for sub_col in self.solve_col:
                for item in sub_col:
                    if item == '1':
                        self.one_solve_col_index = self.solve_col.index(sub_col)
                        self.one_sub_col_index = sub_col.index(item)

            #*The boolean variables will check what kind of motion I can make.

            #*The blacklist_bool stores all the moves that cannot be made
            blacklist_bool = []
            up_bool = True and check_up_bool
            down_bool = True and check_down_bool
            left_bool = True and check_left_bool
            right_bool = True and check_right_bool
            #*At this point, right bool is true
            #*Filter based on position.
            if self.nine_solve_row_index == 2:
                up_bool = False
                blacklist_bool.append(up_bool)
            if self.nine_solve_row_index == 0:
                down_bool = False   
                blacklist_bool.append(down_bool)
            if self.nine_solve_col_index == 2:
                left_bool = False
                blacklist_bool.append(left_bool)
            if self.nine_solve_col_index == 0:
                right_bool = False
                blacklist_bool.append(right_bool)
            '''
            For this algorithm, I have to check for the following.
            1. Whether the empty 9 is next to the 1.
                if it is beneficial to move (getting closer to goal), then move
                else, don't move. Make a variable to note to never move in that way.
            
            2. If the space is losing in row or column, try to improve the space
            if the space is already winning in row, try to improve column and vice versa

            3. If the space is winning in both column and rows, I will need to bring the space closer to 1.

            4. Conedering the non beneficial 1 move, if there are no other beneficial moves for the space, move 
            wherever possible.
            e.g. when the row list is [[2,1,9][7,3,8][5,6,4]], there aren't any beneficial steps neither for 1 and 
            the space so I have to move the 8 up.`
            '''
            #*Covers the win/equal and lose/equal scenarios
            #*All cases for 1 being next to 9
            if self.one_solve_row_index == self.nine_solve_row_index  or self.nine_solve_col_index == self.one_solve_col_index:
                #?Somehow, the solve indexes are not updating properly.
                print(self.one_solve_row_index)
                print(self.nine_solve_row_index)
                #*Beneficial cases (checking whether they are right next to each other)
                #*Covers parat of the Win/equal scenario(When open is left of 1)
                if self.nine_sub_row_index + 1 == self.one_sub_row_index and left_bool:
                    #*Switching the places
                    mut_1 = self.solve_row[self.one_solve_row_index][self.one_sub_row_index]
                    mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                    self.solve_row[self.one_solve_row_index][self.one_sub_row_index] = mut_9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = mut_1
                    self.solve_col[self.one_solve_col_index][self.one_sub_col_index] = mut_9
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = mut_1
                    #*I think I can use continue for these cases because I want to restart after I make one move.
                    #continue
                    
                #*Covers part of the win equal scenario(When open is above 1)
                elif self.nine_sub_col_index + 1 == self.one_sub_col_index and up_bool:
                    mut_1 = self.solve_col[self.one_solve_col_index][self.one_sub_col_index]
                    mut_9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                    self.solve_col[self.one_solve_col_index][self.one_sub_col_index] = mut_9
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = mut_1
                    self.solve_row[self.one_solve_row_index][self.one_sub_row_index] = mut_9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = mut_1
                    #continue

                #*When open wins by 2 columns (on same row)
                elif self.nine_sub_row_index + 2 == self.one_sub_row_index and left_bool:
                    mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                    other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9
                    #continue

                #*When open wins by 2 rows (on same column)
                elif self.nine_sub_col_index + 2 == self.one_sub_col_index and up_bool:
                    mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                    other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9
                    #continue

                #*When open loses by 2 columns (on same row)
                elif self.nine_sub_row_index - 2 == self.one_sub_row_index and down_bool:
                    mut9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                    other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1]
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                    #continue

                #*When open loses by 2 rows (on same column)
                elif self.nine_sub_col_index - 2 == self.one_sub_col_index and down_bool:
                    mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                    other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9
                    #continue

                #*Non-beneficial cases
                elif self.nine_sub_row_index == self.one_sub_row_index + 1:
                    #!In these two cases, I wouldn't add a continue because no change has been made to the list yet.
                    #*In this case, I think I already know what options are the best.
                    #!I think I have to prevent the situation from going back to this place in the future.
                    if down_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9
                        check_up_bool = False
                        print("passed")
                        

                    #*I think left is never possible for any case. down and up will cover everything.

                    elif up_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9       
                        #!Since this is not a beneficial move, I am going to change check booleans
                        check_down_bool = False
                        #*But I will have to make sure this resets to True after the next move.                                     
                    

                elif self.nine_sub_col_index == self.one_sub_col_index + 1:
                    down_bool = False
                    blacklist_bool.append(down_bool)
                    if right_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9
            
                    #*I think up is never possible for any case. Right and left will cover everything.
                    elif left_bool:
                        mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                        other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9
                        check_right_bool = False
                        #*I have to make sure to reset this too.
            
            #*The lose lose scenario
            
            elif self.nine_solve_row_index > self.one_solve_row_index and self.nine_solve_col_index > self.one_solve_col_index:

                if (self.nine_solve_row_index - self.one_solve_row_index) < (self.nine_solve_col_index - self.one_solve_col_index):
                    if down_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9 

                    #*I think this is pretty unlikely.
                    elif right_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9


                elif (self.nine_solve_row_index - self.one_solve_row_index) > (self.nine_solve_col_index - self.one_solve_col_index):
                    if right_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9
                    
                    #*Pretty unlikely
                    elif down_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9 
                    
                #*I have to add case for same distance
                elif (self.nine_solve_row_index - self.one_solve_row_index) == (self.nine_solve_col_index - self.one_solve_col_index):
                    if down_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9 

                    #*Unlikely
                    elif right_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9


            #*The win, win scenario
            elif self.nine_solve_row_index < self.one_solve_row_index and self.nine_solve_col_index < self.one_solve_col_index:
                if (self.one_solve_row_index - self.nine_solve_row_index) < (self.one_solve_col_index - self.nine_solve_col_index):
                    if up_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9   
                    
                    #*Unlikely
                    elif left_bool:
                        mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                        other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9

                elif (self.one_solve_row_index - self.nine_solve_row_index) > (self.one_solve_col_index - self.nine_solve_col_index):
                    if left_bool:
                        mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                        other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9

                    #*unlikely
                    elif up_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9                     

                elif (self.one_solve_row_index - self.nine_solve_row_index) == (self.one_solve_col_index - self.nine_solve_col_index):
                    if up_bool:
                        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9   
                    
                    #*Unlikely 
                    elif left_bool:
                        mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
                        other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
                        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                        self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9

            #*The win lose scenarios
            elif (self.nine_solve_row_index < self.one_solve_row_index and self.nine_solve_col_index > self.one_solve_col_index):
                if right_bool:
                    mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                    other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9
                #?I don't think there are any other options.
            
            elif (self.nine_solve_row_index > self.one_solve_row_index and self.nine_solve_col_index < self.one_solve_col_index):
                if down_bool:
                    mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
                    other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
                    self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
                    self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
                    self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9 
            print(up_bool)
            print(down_bool)
            print(left_bool)
            print(right_bool)
            print(self.solve_row)
            print(self.solve_col)
            
        print("finished loop")
            

    def solve_2_3(self):
        pass

    def solve_4_7(self):
        pass

    def solve_rest(self):
        pass

            


setupwindow = Tk()
setupwindow.title("Setup Window")
a = SetupWindow(setupwindow)

mainloop()