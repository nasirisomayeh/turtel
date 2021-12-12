# turtle.py
import random as rnd
import turtle
color = ["red","blue","purple","green","yellow","brown"]
spiral = turtle.Turtle()
for i in range(35):
    spiral.pencolor(color[rnd.randint(0,5)])
    spiral.forward(i*10)
    spiral.right(144)
turtle.done()
