
from turtle import forward, right, left
from turtle import exitonclick, shape, goto, penup, pendown
from math import sqrt
#from random import randint
import random


shape('turtle')
penup()
goto(-400,0)
pendown()

def draw_house(a):
    c = sqrt(2*a**2)

    # obvodove steny
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)

    # pricka
    left(90+45)
    forward(c)

    # strecha - TODO komin
    left(90)
    forward(c/2)
    left(90)
    forward(c/2)

    # pricka
    left(90)
    forward(c)
    left(45)


for i in range(10):
    draw_house(random.randint(50, 150))

exitonclick()

