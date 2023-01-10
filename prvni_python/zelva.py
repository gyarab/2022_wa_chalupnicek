from turtle import exitonclick
from turtle import forward, left, goto
from turtle import penup, pendown
from math import sqrt


def draw_house(a):
    c = round(sqrt(2*a**2))
    
    # obvodove steny
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    left(90)
    forward(a)
    
    # pricka ve stene
    left(90+45)
    forward(c)
    left(90)

    # strecha - TODO komin
    forward(c/2)
    left(90)
    forward(c/2)
    left(90)

    # druha pricka ve stene
    forward(c)
    left(45)

# posunout zacatek doleva
penup()
goto(-400, 0)
pendown()

# generovat domecky - TODO nahodne velikosti
draw_house(100)
draw_house(20)
draw_house(60)
draw_house(80)

exitonclick()
