import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
t.speed(1000)
def rectangle(x):
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)

def triangle(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)


def square(x,y):
    for i in range(4):
        t.forward(x)
        t.left(y)

def star(x):
    for i in range(5):
        t.forward(x)
        t.left(144)

def doubleSquares(iRange):
    length = 5
    for i in range(iRange):
        square(length, 90)
        length = length+5
        t.left(5)


def doubleStar(iRange):
    length = 10
    for i in range(iRange):
        star(length)
        length = length+5
        t.left(5)
doubleStar(60)

turtle.done()