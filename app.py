import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
def rectangle(x):
    forward(x)
    left(90)
    forward(100)
    left(90)
    forward(x)
    left(90)
    forward(100)
    left(90)
rectangle(125)
def triangle(x):
    forward(x)
    left(120)
    forward(x)
    left(120)
    forward(x)
triangle(90)    
turtle.done()