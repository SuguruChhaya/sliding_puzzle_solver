from tkinter import *

root = Tk()
root.title("Set up window")

def start():
    root.destroy()

info_text = "Welcome to number setup window!!\n Select the dimensions and the\n speed of explanation."
info_label = Label(root, text=info_text)
info_label.grid(row=0, column=0)

dimension_label = Label(root, text="Dimensions:")
dimension_label.grid(row=1, column=0)

dimension = StringVar()
dimension.set("3x3")
speed = StringVar()
speed.set("3sec")

dimension_list = ["3x3", "4x4", "5x5"]
dimension_dropdown = OptionMenu(root, dimension, *dimension_list)
dimension_dropdown.grid(row=2, column=0)

speed_label = Label(root, text="Speed of explanation\n(Seconds per move):")
speed_label.grid(row=3, column=0)

speed_list = ["1sec", "2sec", "3sec", "4sec", "5sec"]
speed_dropdown = OptionMenu(root, speed, *speed_list)
#*I can use ipad to resize the stuff.
speed_dropdown.grid(row=4, column=0, ipadx=20, ipady=20)



start_button = Button(root, text="Start!!", width=10, height=2, bg="orange", command=start)
start_button.grid(row=5, column=0)



mainloop()