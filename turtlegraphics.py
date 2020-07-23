import turtle
from tkinter import Canvas

a = turtle.Turtle()
a.write("Hi")
b = turtle.Turtle()
b.shape("square")
b.speed(1)
b.goto(-100, 0)
if b.pos() == (-100, 0):
    print("yeet")
a.speed(1)
#*I can use these commands to move the sliders how I want.
a.right(180)
a.forward(30)

next = True
#*The screen is divided into four quadrants.

