from tkinter import *
import tkinter.font

root = Tk()

def move():
    my_canvas.move(a, 100, 0)
    #my_canvas.move(b, 30, 40)
    #*Somehow, the text prefers to move with all the other things. The following line makes it possible.
    my_canvas.move(b, 100, 0)

my_canvas = Canvas(root, width=1000, height=600)
my_canvas.grid(row=0, column=0)

b = my_canvas.create_rectangle(200,400,500,200)
a = my_canvas.create_text(100, 100, text="Hi", font= tkinter.font.Font(size=20), stipple="gray25")

move_button = Button(root, text="move", command=move)
move_button.grid(row=1, column=0)

mainloop() 