from tkinter import *
import tkinter.font
import pygame
pygame.init()
from pygame import mixer
mixer.init()

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

        self.dimension_list = ["3x3"]
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
        a.check_inversion()

#*The following class is just for solving the algorithm and doesn't create any graphics.
class Solve():
    instruction_list = []
    def __init__(self):
        #*I can successfully get the values of the class variables.
        self.solve_row = [[MainWindow.A1.get(), MainWindow.A2.get(), MainWindow.A3.get()], 
                        [MainWindow.B1.get(), MainWindow.B2.get(), MainWindow.B3.get()], 
                        [MainWindow.C1.get(), MainWindow.C2.get(), MainWindow.C3.get()]]
        
        self.solve_col = [[MainWindow.A1.get(), MainWindow.B1.get(), MainWindow.C1.get()],
                        [MainWindow.A2.get(), MainWindow.B2.get(), MainWindow.C2.get()],
                        [MainWindow.A3.get(), MainWindow.B3.get(), MainWindow.C3.get()]]

        #*Converting the "OPEN" to '9' for future convenience
        #!The reason why the nine index is not updated is because I didn't include finding it in my while loop.
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


    def check_inversion(self):
        #!I will make a function to check for the number of inversions to see if the puzzle can actually be solved.
        #*Check out https://www.geeksforgeeks.org/counting-inversions/#:~:text=%20%20%201%20Approach%3A%0ASuppose%20the%20number%20of,the%20base...%204%20Print%20the%20answer%20More%20
        #*and https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
        #*The problem arises when I try to solve for 2 and 3.

        #*Convert self.solve_row into a one-dimensional list, cast them to an integer, and remove nine.
        check_list = []
        for sub_list in self.solve_row:
            for item in sub_list:
                if item != "9":
                    check_list.append(int(item))
        
        inversion_count = 0
        for i in range(len(check_list)):
            for j in range(i + 1, len(check_list)):
                if check_list[i] > check_list[j]:
                    inversion_count += 1
        
        if inversion_count % 2 == 0:
            self.solve_1()
        else:
            error = Tk()
            self.cannot_solve(error)

    def cannot_solve(self, root):
        error_font = tkinter.font.Font(size=60, weight="bold")
        Label(root, text="Puzzle cannot be solved!!", font=error_font, fg="red").pack()

    def find_nine(self):
        for sub_row in self.solve_row:
            for item in sub_row:
                if item == "9":
                    self.nine_solve_row_index = self.solve_row.index(sub_row)
                    self.nine_sub_row_index = sub_row.index(item)

        for sub_col in self.solve_col:
            for item in sub_col:
                if item == "9":
                    self.nine_solve_col_index = self.solve_col.index(sub_col)
                    self.nine_sub_col_index = sub_col.index(item)

    def solve_1(self):
        #*A class variable list to track everything we did. Can be accessed from other classes.
        #!The following variables keep track of which ways I should not move to.
        #*By emptying the list, I can remake the list as many times as I want.
        Solve.instruction_list = []
        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True
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

            self.find_nine()

            #*The boolean variables will check what kind of motion I can make.


            #*At this point, right bool is true
            #*Filter based on position.
            if self.nine_solve_row_index == 2:
                up_bool = False
            if self.nine_solve_row_index == 0:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            if self.nine_solve_col_index == 0:
                right_bool = False
        
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
                #*Beneficial cases (checking whether they are right next to each other)
                #*Covers parat of the Win/equal scenario(When open is left of 1)
                if self.nine_sub_row_index + 1 == self.one_sub_row_index and left_bool:
                    #*Switching the places
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
                    
                #*Covers part of the win equal scenario(When open is above 1)
                elif self.nine_sub_col_index + 1 == self.one_sub_col_index and up_bool:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*When open wins by 2 columns (on same row)
                elif self.nine_sub_row_index + 2 == self.one_sub_row_index and left_bool:
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*When open wins by 2 rows (on same column)
                elif self.nine_sub_col_index + 2 == self.one_sub_col_index and up_bool:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*When open loses by 2 columns (on same row)
                elif self.nine_sub_row_index - 2 == self.one_sub_row_index and down_bool:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*When open loses by 2 rows (on same column)
                elif self.nine_sub_col_index - 2 == self.one_sub_col_index and down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*Non-beneficial cases
                elif self.nine_sub_row_index == self.one_sub_row_index + 1:
                    #!In these two cases, I wouldn't add a continue because no change has been made to the list yet.
                    #*In this case, I think I already know what options are the best.
                    #!I think I have to prevent the situation from going back to this place in the future.
                    if down_bool:
                        self.solve_1_down()
                        up_bool = False
                        #*I think I should reset everything else to true at every end of the while loop.
                        #*I should make the variables self and create a function for this so it is easier.
                        down_bool = True
                        left_bool = True
                        right_bool = True
                        

                    #*I think left is never possible for any case. down and up will cover everything.

                    elif up_bool:
                        self.solve_1_up()
                        #!Since this is not a beneficial move, I am going to change check booleans
                        down_bool = False
                        up_bool = True
                        left_bool = True
                        right_bool = True

                        #*But I will have to make sure this resets to True after the next move.                                     
                    

                elif self.nine_sub_col_index == self.one_sub_col_index + 1:

                    if right_bool:
                        self.solve_1_right()
                        left_bool = False
                        up_bool = True
                        down_bool = True
                        right_bool = True


            
                    #*I think up is never possible for any case. Right and left will cover everything.
                    elif left_bool:
                        self.solve_1_left()
                        right_bool = False
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        

                        #*I have to make sure to reset this too.
            
            #*The lose lose scenario
            
            elif self.nine_solve_row_index > self.one_solve_row_index and self.nine_solve_col_index > self.one_solve_col_index:

                if (self.nine_solve_row_index - self.one_solve_row_index) < (self.nine_solve_col_index - self.one_solve_col_index):
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    #*I think this is pretty unlikely.
                    elif right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True


                elif (self.nine_solve_row_index - self.one_solve_row_index) > (self.nine_solve_col_index - self.one_solve_col_index):
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                    #*Pretty unlikely
                    elif down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                #*I have to add case for same distance
                elif (self.nine_solve_row_index - self.one_solve_row_index) == (self.nine_solve_col_index - self.one_solve_col_index):
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    #*Unlikely
                    elif right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True


            #*The win, win scenario
            elif self.nine_solve_row_index < self.one_solve_row_index and self.nine_solve_col_index < self.one_solve_col_index:
                if (self.one_solve_row_index - self.nine_solve_row_index) < (self.one_solve_col_index - self.nine_solve_col_index):
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                    #*Unlikely
                    elif left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                elif (self.one_solve_row_index - self.nine_solve_row_index) > (self.one_solve_col_index - self.nine_solve_col_index):
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    #*unlikely
                    elif up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True              

                elif (self.one_solve_row_index - self.nine_solve_row_index) == (self.one_solve_col_index - self.nine_solve_col_index):
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                    #*Unlikely 
                    elif left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

            #*The win lose scenarios
            elif (self.nine_solve_row_index < self.one_solve_row_index and self.nine_solve_col_index > self.one_solve_col_index):
                if right_bool:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
                #?I don't think there are any other options.
            
            elif (self.nine_solve_row_index > self.one_solve_row_index and self.nine_solve_col_index < self.one_solve_col_index):
                if down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
        
        print(self.solve_row)
        print(self.solve_col)
        #*Check whether step necessary.
        if self.solve_row[0][1] == '2' and self.solve_row[0][2] == '3':
            self.solve_4_7()
        else:
            self.solve_2()

    def solve_1_up(self):
        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1]
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index + 1] = mut9
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
        self.solve_row[self.nine_solve_row_index + 1][self.nine_sub_row_index] = mut9  
        Solve.instruction_list.append("up")   

    def solve_1_down(self):
        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
        other = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1]
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index - 1] = mut9
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
        self.solve_row[self.nine_solve_row_index - 1][self.nine_sub_row_index] = mut9
        Solve.instruction_list.append("down")

    def solve_1_left(self):
        mut_9 = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index]
        other = self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1]
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index + 1] = mut_9
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
        self.solve_col[self.nine_solve_col_index + 1][self.nine_sub_col_index] = mut_9
        Solve.instruction_list.append("left")

    def solve_1_right(self):
        mut9 = self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index]
        other = self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index]
        self.solve_col[self.nine_solve_col_index][self.nine_sub_col_index] = other
        self.solve_col[self.nine_solve_col_index - 1][self.nine_sub_col_index] = mut9
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index] = other
        self.solve_row[self.nine_solve_row_index][self.nine_sub_row_index - 1] = mut9
        Solve.instruction_list.append("right")

#*I should show the code for improved reference.
    '''
    def solve_2_3_intro(self):
        #*I am going to find out which solving appraoch (2 or 3) is better.
        #*For that, I am first going to find their location.
        for sub_row in self.solve_row:
            for item in sub_row:
                if item == '2':
                    two_current_first_row = self.solve_row.index(sub_row)
                    two_current_second_row = sub_row.index(item)
                elif item == '3':
                    three_current_first_row = self.solve_row.index(sub_row)
                    three_current_second_row = sub_row.index(item)
        
        #*Finding distance.
        two_distance = abs(0 - two_current_first_row) + abs(2 - two_current_second_row)
        three_distance = abs(0 - three_current_first_row) + abs(1 - three_current_second_row)

        if two_distance < three_distance:
            self.solve_2()
        elif two_distance > three_distance:
            self.solve_3()
        elif two_distance == three_distance:
            for nest_row in self.solve_row:
                for item in nest_row:
                    if item == '9':
                        nine_first_row = self.solve_row.index(nest_row)
                        nine_second_row = nest_row.index(item)
            
            two_distance = abs(nine_first_row - two_current_first_row) + abs(nine_second_row - two_current_second_row)
            three_distance = abs(nine_first_row - three_current_first_row) + abs(nine_second_row - three_current_second_row)
            if two_distance < three_distance:
                self.solve_2()
            elif two_distance > three_distance:
                self.solve_3()
    '''
    def solve_2(self):
        #*Creating the booleans again.
        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True
        while self.solve_row[0][2] != '2':
            #*I should definitely refactor the code for nine later on.
            for sub_row in self.solve_row:
                for item in sub_row:
                    if item == '2':
                        self.two_solve_row_index = self.solve_row.index(sub_row)
                        self.two_sub_row_index = sub_row.index(item)

            #*I honestly don't know if I am going to need a column explanation but I am just going to add it there.
            for sub_col in self.solve_col:
                for item in sub_col:
                    if item == '2':
                        self.two_solve_col_index = self.solve_col.index(sub_col)
                        self.two_sub_col_index = sub_col.index(item)

            self.find_nine()

            if self.nine_solve_row_index == 2:
                up_bool = False
            if self.nine_solve_row_index == 0:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            if self.nine_solve_col_index == 0:
                right_bool = False
            
            #*To prevent 1 from moving
            if self.solve_row[0][1] == '9':
                right_bool = False

            if self.solve_row[1][0] == '9':
                down_bool = False

            #*On the same row.
            if self.two_solve_row_index == self.nine_solve_row_index  or self.two_solve_col_index == self.nine_solve_col_index:
                #*location of nine winning by 1 column (same row)
                if self.nine_solve_col_index -1 == self.two_solve_col_index:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*9 wins by one row (same column)
                elif self.nine_solve_row_index + 1 == self.two_solve_row_index:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*9 is closer to 2's goal position by 2 columns(same row)
                elif self.nine_solve_col_index - 2 == self.two_solve_col_index:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*9 is winning by 2 rows (same columns)
                #*move up
                elif self.nine_solve_row_index + 2 == self.two_solve_row_index:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*9 is losing by 2 columns (same row)
                elif self.nine_solve_col_index + 2 == self.two_solve_col_index:
                    #*Move left
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
                
                #*9 is losing by 2 rows (same column)
                elif self.nine_solve_row_index - 2 == self.two_solve_row_index:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                #*Non-beneficial cases.
                #*9 is losing by 1 column(same row)
                elif self.nine_solve_col_index + 1 == self.two_solve_col_index:
                    if down_bool:
                        self.solve_1_down()
                        up_bool = False
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    elif up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = False
                        left_bool = True
                        right_bool = True
                
                #*9 is losing by 1 row(same column)
                elif self.nine_solve_row_index - 1 == self.two_solve_row_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = False
                    
                    elif right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = False
                        right_bool = True

            #*The lose lose scenario
            elif self.nine_solve_row_index > self.two_solve_row_index and self.nine_solve_col_index < self.two_solve_col_index:
                #*Better to allign 9 onto same row as 2
                if (self.nine_solve_row_index - self.two_solve_row_index) < (self.two_solve_col_index - self.nine_solve_col_index):
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*Better to allign 9 onto same column as 2
                elif (self.nine_solve_row_index - self.two_solve_row_index) > (self.two_solve_col_index - self.nine_solve_col_index):
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                elif (self.nine_solve_row_index - self.two_solve_row_index) == (self.two_solve_col_index - self.nine_solve_col_index):
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    elif left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

            #*The win win scenario
            elif self.nine_solve_row_index < self.two_solve_row_index and self.nine_solve_col_index > self.two_solve_col_index:
                if self.two_solve_row_index - self.nine_solve_row_index < self.nine_solve_col_index - self.two_solve_col_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True                
                    
                elif self.two_solve_row_index - self.nine_solve_row_index > self.nine_solve_col_index - self.two_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    elif up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                elif self.two_solve_row_index - self.nine_solve_row_index == self.nine_solve_col_index - self.two_solve_col_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True  
                    
                    elif right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True  

            #*The win lose scenarios
            elif self.nine_solve_row_index < self.two_solve_row_index and self.two_solve_col_index > self.nine_solve_col_index:
                if left_bool:
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True  
            
            elif self.nine_solve_row_index > self.two_solve_row_index and self.two_solve_col_index < self.nine_solve_col_index:
                if down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True  


            
        print(self.solve_row)
        print(self.solve_col)

        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True
        #*After exiting the previous while loop, I now have to place 3 below 2.
        while self.solve_row[1][2] != '3':
            for sub_row in self.solve_row:
                for item in sub_row:
                    if item == '3':
                        self.three_solve_row_index = self.solve_row.index(sub_row)
                        self.three_sub_row_index = sub_row.index(item)

            #*I honestly don't know if I am going to need a column explanation but I am just going to add it there.
            for sub_col in self.solve_col:
                for item in sub_col:
                    if item == '3':
                        self.three_solve_col_index = self.solve_col.index(sub_col)
                        self.three_sub_col_index = sub_col.index(item)
            self.find_nine()

            if self.nine_solve_row_index == 2:
                up_bool = False
            if self.nine_solve_row_index == 0:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            if self.nine_solve_col_index == 0:
                right_bool = False
            
            #*To prevent 1 from moving
            if self.solve_row[0][1] == '9':
                #*Now I also have to consider the 2.
                left_bool = False
                right_bool = False

            if self.solve_row[1][0] == '9':
                down_bool = False

            if self.solve_row[1][2] == '9':
                down_bool = False

            if self.nine_solve_row_index == self.three_solve_row_index or self.nine_solve_col_index == self.three_solve_col_index:
                #*On same row, nine winning by one.
                if self.nine_solve_col_index - 1 == self.three_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*On same column, nine winning by one row.
                elif self.nine_solve_row_index + 1 == self.three_solve_row_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is closer to 3's goal position by 2 columns (same row)
                #!I do have to make the 2 row version for when they are on the middle column
                elif self.nine_solve_col_index - 2 == self.three_solve_col_index:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                elif self.nine_solve_row_index + 2 == self.three_solve_row_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True                

                #*Non-beneficial cases.
                #*9 is losing by 1 column(same row)
                elif self.nine_solve_col_index + 1 == self.three_solve_col_index:
                    if down_bool:
                        self.solve_1_down()
                        up_bool = False
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                    elif up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = False
                        left_bool = True
                        right_bool = True
                
                #*9 is losing by 1 row(same column)
                elif self.nine_solve_row_index - 1 == self.three_solve_row_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = False

            #*The lose lose scenario
            #*These scenarios are pretty unrealistic but I included them
            elif self.nine_solve_row_index > self.three_solve_row_index and self.nine_solve_col_index < self.three_solve_col_index:
                #*Better allign 9 onto the same row as 3
                if (self.nine_solve_row_index - self.three_solve_row_index) < (self.three_solve_col_index - self.nine_solve_col_index):
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                elif (self.nine_solve_row_index - self.three_solve_row_index) > (self.three_solve_col_index - self.nine_solve_col_index):
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                elif (self.nine_solve_row_index - self.three_solve_row_index) == (self.three_solve_col_index - self.nine_solve_col_index):
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    elif down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True   

            
            #*The win win scenario
            elif self.nine_solve_row_index < self.three_solve_row_index and self.nine_solve_col_index > self.three_solve_col_index:
                if self.three_solve_row_index - self.nine_solve_row_index < self.nine_solve_col_index - self.three_solve_col_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True 

                elif self.three_solve_row_index - self.nine_solve_row_index > self.nine_solve_col_index - self.three_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True 

                    #*Just in case 9 is in the middle of the first row.
                    elif up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True                 

                elif self.three_solve_row_index - self.nine_solve_row_index == self.nine_solve_col_index - self.three_solve_col_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True  

                    elif right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

            #*The win lose scenarios
            elif self.nine_solve_row_index < self.three_solve_row_index and self.three_solve_col_index > self.nine_solve_col_index:
                if left_bool:
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True  

            elif self.nine_solve_row_index > self.three_solve_row_index and self.three_solve_col_index < self.nine_solve_col_index:
                if down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True  
                
        
        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True

        print(self.solve_row)
        print(self.solve_col)

        
        if not (self.solve_row[0][1] == '2' and self.move[0][2] == '3'):
            self.find_nine()

            if self.solve_row[2][2] == '9':
                self.solve_1_right()
                self.find_nine()
                self.solve_1_down()

            self.find_nine()
            self.solve_1_down()
            self.find_nine()
            self.solve_1_left()
            self.find_nine()
            self.solve_1_up()
            self.solve_4_7()

    def find_four(self):
        for sub_row in self.solve_row:
                        for item in sub_row:
                            if item == '4':
                                self.four_solve_row_index = self.solve_row.index(sub_row)
                                self.four_sub_row_index = sub_row.index(item)

        for sub_col in self.solve_col:
            for item in sub_col:
                if item == '4':
                    self.four_solve_col_index = self.solve_col.index(sub_col)
                    self.four_sub_col_index = sub_col.index(item)

    def find_seven(self):
        for sub_row in self.solve_row:
            for item in sub_row:
                if item == '7':
                    self.seven_solve_row_index = self.solve_row.index(sub_row)
                    self.seven_sub_row_index = sub_row.index(item)

        for sub_col in self.solve_col:
            for item in sub_col:
                if item == '7':
                    self.seven_solve_col_index = self.solve_col.index(sub_col)
                    self.seven_sub_col_index = sub_col.index(item)

    def solve_4_7(self):
        #*I have to first make sure 4 is not in the first column
        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True
        while '4' in self.solve_col[0]:
            
            self.find_four()
            self.find_nine()

            if self.nine_solve_row_index == 2:
                up_bool = False

            #*Since 1,2, and 3 are already set, down bool must be false in this case.
            if self.nine_solve_row_index == 1:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            if self.nine_solve_col_index == 0:
                right_bool = False

            
            #*On the same row or column
            if self.four_solve_row_index == self.nine_solve_row_index or self.four_solve_col_index == self.nine_solve_col_index:
                #*9 winning by 1 column(can help four get out of first column)
                if self.four_solve_col_index + 1 == self.nine_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*Since we are not interested in moving 4 up or down, so I don't think I need
                #*to add anything else.

                #*When 9 is winning by 2 columns (same row)
                elif self.nine_solve_col_index - 2 == self.four_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*Because of the condition of this loop, it is impossible for 9 to lose by 2 columns. 

                #*Non-beneficial cases.
                elif self.four_solve_row_index + 1 == self.nine_solve_row_index or self.four_solve_row_index - 1 == self.nine_solve_row_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = False

                #*Lose lose scenarios aren't possible when 4 is in the first column.

            #*The win win scenario(will always have to move up)
            elif self.nine_solve_row_index < self.four_solve_row_index and self.nine_solve_col_index > self.four_solve_col_index:
                if up_bool:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

            #*The win lose scenario
            elif self.nine_solve_row_index > self.four_solve_row_index and self.nine_solve_col_index > self.four_solve_col_index:
                if down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
            
        print(self.solve_row)
        print(self.solve_col)
        print(Solve.instruction_list)

        up_bool = True
        down_bool = True
        left_bool = True
        right_bool = True

        while self.solve_row[1][0] != '7':
            self.find_four()
            self.find_nine()
            self.find_seven()

            if self.nine_solve_row_index == 2:
                up_bool = False
            if self.nine_solve_row_index == 1:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            if self.nine_solve_col_index == 0:
                right_bool = False

            #*Make sure 4 doesn't move to the left.
            if self.nine_solve_row_index == self.four_solve_row_index and self.nine_solve_col_index + 1 == self.four_solve_col_index:
                left_bool = False

            #*Make sure four doesn't move down (e.g. [[1,2,3], [8,4,6], [7,9,5]])
            if self.solve_row[1][1]== '4' and self.solve_row[2][1] == '9':
                down_bool = False

            #*On same row or column
            if self.nine_solve_row_index == self.seven_solve_row_index or self.nine_solve_col_index == self.seven_solve_col_index:
                #*Beneficial moves
                #*9 is above 7
                if self.nine_solve_row_index + 1 == self.seven_solve_row_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is left of 7
                elif self.nine_solve_col_index + 1 == self.seven_solve_col_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is winning by 2 columns to 7
                elif self.nine_solve_col_index + 2 == self.seven_solve_col_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                    
                    #*In case 4 is in between
                    elif up_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is losing by 2 columns to 7
                elif self.nine_solve_col_index - 2 == self.seven_solve_col_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    #*In case of example like 1,2,3,8,4,6,7,9,5 after the non-beneficial move
                    elif down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True     

                #*Because the first row is fixed, 9 cannot win or lose by 2 rows

                #*Non-beneficial cases
                #*9 is below 7(same column)
                elif self.nine_solve_row_index - 1 == self.seven_solve_row_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = False
                        right_bool = True

                #*9 is right to 7(same row)
                elif self.nine_solve_col_index - 1  == self.seven_solve_col_index:
                    if down_bool:
                        self.solve_1_down()
                        up_bool = False
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    #*For when 4 is above 9 (e.g. 1,2,3,8,4,6,7,9,5)
                    elif left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = False

            #*Lose lose scenario
            #*Even there are 1)better allign row and 2) equal distance scenario
            #*I think they both prefer right
            elif self.nine_solve_row_index > self.seven_solve_row_index and self.nine_solve_col_index > self.seven_solve_col_index:
                if right_bool:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

            #*The win win scenario
            #*Even though there are two scenarios here too, I think up and left can take it.
            elif self.nine_solve_row_index < self.seven_solve_row_index and self.nine_solve_col_index < self.seven_solve_col_index:
                if up_bool:
                    self.solve_1_up()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

                elif left_bool:
                    self.solve_1_left()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

            #*The win lose scenario
            #*9 wins in terms of rows, loses in terms of columns
            elif self.nine_solve_row_index < self.seven_solve_row_index and self.nine_solve_col_index > self.seven_solve_col_index:
                if right_bool:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

            #*9 wins in terms of columns, loses in terms of rows
            elif self.nine_solve_row_index > self.seven_solve_row_index and self.nine_solve_col_index < self.seven_solve_col_index:
                if down_bool:
                    self.solve_1_down()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True
                
                elif right_bool:
                    self.solve_1_right()
                    up_bool = True
                    down_bool = True
                    left_bool = True
                    right_bool = True

            

        print(self.solve_row)
        print(self.solve_col)
        print(Solve.instruction_list)
        

        #*Put 4 next to 7
        while self.solve_row[1][1] != '4':
            self.find_nine()
            self.find_four()

            if self.nine_solve_row_index == 2:
                up_bool = False
            if self.nine_solve_row_index == 1:
                down_bool = False   
    
            if self.nine_solve_col_index == 2:
                left_bool = False
    
            #*Because the first column is only occupied by the 7 and a non-4.
            if self.nine_solve_col_index == 1:
                right_bool = False

            #*On same row or column
            if self.nine_solve_row_index == self.four_solve_row_index or self.nine_solve_col_index == self.four_solve_col_index:
                #*9 is left of 4
                if self.nine_solve_col_index + 1 == self.four_solve_col_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                #*9 is above 4
                elif self.nine_solve_row_index + 1 == self.four_solve_row_index:
                    if up_bool:
                        self.solve_1_up()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is winning by 2 rows (not posssible)

                #* 9 is winning by 2 columns
                elif self.nine_solve_col_index + 2 == self.four_solve_col_index:
                    if left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True
                
                #*9 is losing by 2 rows (not possible)

                #*9 is losing by 2 columns (not possible because 4 will never get into this position)

                #*Non-beneficial cases
                #*9 is losing by one row (same column)
                elif self.nine_solve_col_index - 1 == self.four_solve_col_index:
                    if down_bool:
                        self.solve_1_down()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                #*9 is losing by one column (same row)
                elif self.nine_solve_row_index - 1 == self.four_solve_row_index:
                    if right_bool:
                        self.solve_1_right()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

                    elif left_bool:
                        self.solve_1_left()
                        up_bool = True
                        down_bool = True
                        left_bool = True
                        right_bool = True

            

            break



    def solve_rest(self):
        pass

    def gotoMovetiles(self):
        print(Solve.instruction_list)
        solvewindow = Tk()
        solvewindow.title("Solving Window")
        a = SolveWindow(solvewindow)
        a.countdown()
        #*Will pass another method



class SolveWindow():
    def __init__(self, root):
        #*Since there was a mutation issue, I am going to repeat the process.
        self.root = root

        self.move_row = [[MainWindow.A1.get(), MainWindow.A2.get(), MainWindow.A3.get()], 
                        [MainWindow.B1.get(), MainWindow.B2.get(), MainWindow.B3.get()], 
                        [MainWindow.C1.get(), MainWindow.C2.get(), MainWindow.C3.get()]]
        
        self.move_col = [[MainWindow.A1.get(), MainWindow.B1.get(), MainWindow.C1.get()],
                        [MainWindow.A2.get(), MainWindow.B2.get(), MainWindow.C2.get()],
                        [MainWindow.A3.get(), MainWindow.B3.get(), MainWindow.C3.get()]]
        for sub_row in self.move_row:
            for item in sub_row:
                if item == "OPEN":
                    self.nine_solve_row_index = self.move_row.index(sub_row)
                    self.nine_sub_row_index = sub_row.index(item)
                    self.move_row[self.nine_solve_row_index][self.nine_sub_row_index] = '9'

        for sub_col in self.move_col:
            for item in sub_col:
                if item == "OPEN":
                    self.nine_solve_col_index = self.move_col.index(sub_col)
                    self.nine_sub_col_index = sub_col.index(item)
                    self.move_col[self.nine_solve_col_index][self.nine_sub_col_index] = '9'

        self.my_canvas = Canvas(self.root, width=300, height=300, bg="white")
        self.my_canvas.grid(row=0, column=0, columnspan=4)

        my_font = tkinter.font.Font(size=30, weight="bold")
        #*I have to make sure the text is assigned in the right place and that self.open9 will be the OPEN space.
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.text4 = ""
        self.text5 = ""
        self.text6 = ""
        self.text7 = ""
        self.text8 = ""
        self.open9 = ""

        self.tags_list = []
        x_counter = 100
        y_counter = 100
        #*I have to figue out an efficient way to manage the variables knowing where what is.
        for sub_row in self.move_row:
            for item in sub_row:
                sub_row_index = self.move_row.index(sub_row)
                item_index = sub_row.index(item)
                item_text = self.move_row[sub_row_index][item_index]
                #?I think my canvas somehow assigns a number starting from 1.
                #!Tkinter canvas assigns the integer for any new items created on the widget.
                #*I might be able to use this to move my widgets around.
                #?If I have to change the variables directly, I don't even think I need a list.
                #?Maybe I could check the item first, then make the text, I will see.
                #*I need to change the variable itself.
                if item == '1':
                    #?Somehow, an int string doesn't really work well
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="one")
                    self.text1 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text1)
                elif item == '2':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="two")
                    self.text2 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text2)
                elif item == '3':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="three")
                    self.text3 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text3)
                elif item == '4':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="four")
                    self.text4 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text4)
                elif item == '5':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="five")
                    self.text5 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text5)
                elif item == '6':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="six")
                    self.text6 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text6)
                elif item == '7':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="seven")
                    self.text7 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text7)
                elif item == '8':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text=item_text, font=my_font, tags="eight")
                    self.text8 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.text8)
                elif item == '9':
                    temp = self.my_canvas.create_text(x_counter, y_counter, text="", font=my_font, tags="nine")
                    self.open9 = self.my_canvas.gettags(temp)[0]
                    self.tags_list.append(self.open9)
                #?Even though I now know how this works, I need it to move the right widgets.
                #?I cannot even get the text of the create_text because it is a complete integer.
                if item_index == 2:
                    x_counter -=60
                    y_counter += 30
                else:
                    x_counter += 30

        #?Ultimately, lists store integers, not variables. Since create_text creates an integer from the first create_text,
        #?I cannot track order. 
        #*I am going to try and use tags to control order I guess.
        self.tags_row_list = [["","",""],["","",""],["","",""]]
        self.tags_col_list = [["","",""],["","",""],["","",""]]
        first_row_counter = 0
        second_row_counter = 0
        first_col_counter = 0
        second_col_counter = 0
        for item in self.tags_list:
            self.tags_row_list[first_row_counter][second_row_counter] = item
            self.tags_col_list[first_col_counter][second_col_counter] = item
            if self.tags_list.index(item) in [2,5,8]:
                first_row_counter += 1
                second_row_counter -= 2
                first_col_counter -= 2
                second_col_counter += 1
            else:
                second_row_counter += 1
                first_col_counter += 1
                
        #*I am going to pre-define it so it doesn' cause any errors later.
        self.in_row_list = None
        self.in_sub_row = None
        self.list_counter = 0
        #*I can use tags to move items.

            #*Find a good way to manage the variables.
        
        #*Since self.text_list is not correctly ordered, I don't think I should use it after ordering everything.
    def countdown(self):
        #*I am making this function because the tiles cannot start moving right after the window pops up.
        #*I am giving 3 second for the tiles to not move.
        #*I think I could just make the instruction list on the right for now.
        
        self.my_canvas.after(3000, self.loop_list)

    def loop_list(self):
        #*I wanted to place a forloop here, but since I had to use the after function, a forloop wont work.
        '''
        for item in Solve.instruction_list:
            if item == "up":
                self.move_up()
            elif item == "down":
                self.move_down()

            elif item == "left":
                self.move_left()

            elif item == "right":
                self.move_right()
        '''
        if self.list_counter < len(Solve.instruction_list):
            if Solve.instruction_list[self.list_counter] == "up":
                self.move_up()
            elif Solve.instruction_list[self.list_counter] == "down":
                self.move_down()
            elif Solve.instruction_list[self.list_counter] == "left":
                self.move_left()
            elif Solve.instruction_list[self.list_counter] == "right":
                self.move_right()
            self.list_counter += 1
            self.after_func = self.my_canvas.after(1000, self.loop_list)
        else:
            #*I am going to unbind the after function here.
            self.my_canvas.after_cancel(self.after_func)
    def move_up(self):
        self.row_func()
        self.col_func()
        mixer.music.load("audio_files/up.mp3")
        mixer.music.play()
        self.my_canvas.move(self.open9, 0, 30)
        self.my_canvas.move(self.tags_row_list[self.in_row_list + 1][self.in_sub_row], 0, -30)
        #!Careful with mutation
        mut1 = self.tags_row_list[self.in_row_list][self.in_sub_row]
        mut2 = self.tags_row_list[self.in_row_list + 1][self.in_sub_row]
        self.tags_row_list[self.in_row_list][self.in_sub_row] = mut2
        self.tags_row_list[self.in_row_list + 1][self.in_sub_row] = mut1
        mut3 = self.tags_col_list[self.in_col_list][self.in_sub_col]
        mut4 = self.tags_col_list[self.in_col_list][self.in_sub_col + 1]
        self.tags_col_list[self.in_col_list][self.in_sub_col] = mut4
        self.tags_col_list[self.in_col_list][self.in_sub_col + 1] = mut3

    def move_down(self):
        self.row_func()
        self.col_func()
        mixer.music.load("audio_files/down.mp3")
        mixer.music.play()
        self.my_canvas.move(self.open9, 0, -30)
        self.my_canvas.move(self.tags_row_list[self.in_row_list - 1][self.in_sub_row], 0, 30)
        mut1 = self.tags_row_list[self.in_row_list][self.in_sub_row]
        mut2 = self.tags_row_list[self.in_row_list - 1][self.in_sub_row]
        self.tags_row_list[self.in_row_list][self.in_sub_row] = mut2
        self.tags_row_list[self.in_row_list - 1][self.in_sub_row] = mut1
        mut3 = self.tags_col_list[self.in_col_list][self.in_sub_col]
        mut4 = self.tags_col_list[self.in_col_list][self.in_sub_col - 1]
        self.tags_col_list[self.in_col_list][self.in_sub_col] = mut4
        self.tags_col_list[self.in_col_list][self.in_sub_col - 1] = mut3

    def move_left(self):
        self.row_func()
        self.col_func()
        mixer.music.load("audio_files/left.mp3")
        mixer.music.play()
        self.my_canvas.move(self.open9, 30, 0)
        self.my_canvas.move(self.tags_col_list[self.in_col_list + 1][self.in_sub_col], -30, 0)
        mut1 = self.tags_col_list[self.in_col_list][self.in_sub_col]
        mut2 = self.tags_col_list[self.in_col_list + 1][self.in_sub_col]
        self.tags_col_list[self.in_col_list][self.in_sub_col] = mut2
        self.tags_col_list[self.in_col_list + 1][self.in_sub_col] = mut1
        mut3 = self.tags_row_list[self.in_row_list][self.in_sub_row]
        mut4 = self.tags_row_list[self.in_row_list][self.in_sub_row + 1]
        self.tags_row_list[self.in_row_list][self.in_sub_row] = mut4
        self.tags_row_list[self.in_row_list][self.in_sub_row + 1] = mut3

    def move_right(self):
        self.row_func()
        self.col_func()
        mixer.music.load("audio_files/right.mp3")
        mixer.music.play()
        self.my_canvas.move(self.open9, -30, 0)
        self.my_canvas.move(self.tags_col_list[self.in_col_list - 1][self.in_sub_col], 30, 0)
        mut1 = self.tags_col_list[self.in_col_list][self.in_sub_col]
        mut2 = self.tags_col_list[self.in_col_list - 1][self.in_sub_col]
        self.tags_col_list[self.in_col_list][self.in_sub_col] = mut2
        self.tags_col_list[self.in_col_list - 1][self.in_sub_col] = mut1
        mut3 = self.tags_row_list[self.in_row_list][self.in_sub_row]
        mut4 = self.tags_row_list[self.in_row_list][self.in_sub_row - 1]
        self.tags_row_list[self.in_row_list][self.in_sub_row] = mut4
        self.tags_row_list[self.in_row_list][self.in_sub_row - 1] = mut3

    def row_func(self):
        for sub_row in self.tags_row_list:
            for item in sub_row:
                if item == self.open9:
                    self.in_row_list = self.tags_row_list.index(sub_row)
                    self.in_sub_row = sub_row.index(item)
                    break

    #Might be able to delete the col func if I find it useless. I will see.
    def col_func(self):
        for sub_col in self.tags_col_list:
            for item in sub_col:
                if item == self.open9:
                    self.in_col_list = self.tags_col_list.index(sub_col)
                    self.in_sub_col = sub_col.index(item)
                    break




        


setupwindow = Tk()
setupwindow.title("Setup Window")
a = SetupWindow(setupwindow)

mainloop()