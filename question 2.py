# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 18:02:55 2020

@author: amand
"""
# Assinment Turtle 
#Question #2
#In a function, create a drawing shape composed of several shapes and colors 
#of your choosing.  Draw the shape randomly on the screen. 
#The user gets to choose how many.


#Amanda Faulconer


import turtle
import random


try:
    sc = turtle.Screen()
    tt = turtle.Turtle()
    
except:
    sc = turtle.Screen()
    tt = turtle.Turtle()

status = True


def triangle(xpos,ypos):

    tt.pu()
    tt.setx(xpos)
    tt.sety(ypos)
    for i in range(3):
        tt.pd()
        tt.forward(200)
        tt.left(120)

def randomPosNeg():
    rn = random.randint(0,100) % 2
    if(rn == 0):
        rn = 1
    else:
        rn = -1
    return rn

def draw_triangle():
    ans = "y"
    while(ans == "y") or (ans == "yes"):
        shape = int(turtle.numinput("count", "Enter number of shapes: "))
        for i in range(shape):
            xpos = random.randint(0, 300) * randomPosNeg()
            ypos = random.randint(0, 300) * randomPosNeg()
            triangle(xpos,ypos)
        ans = turtle.textinput("Quit", "Continue y/n ")

                 
def main():
    
    
    randomPosNeg()
    draw_triangle()
    
    turtle.exitonclick()
    turtle.bye()
    turtle.done()
    
main()
















