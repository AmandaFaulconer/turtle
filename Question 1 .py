# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 17:36:31 2020

@author: amand
"""

#turtle assignment
# question 1
# In a function, draw a scene consisting of several shapes, lines, etc of 
# your choice in the screen. 
#   - more than 2 

# Amanda Faulconer


import turtle


try:
    sc = turtle.Screen()
    tt = turtle.Turtle()
    
except:
    sc = turtle.Screen()
    tt = turtle.Turtle()

status = True

xpos = -249
ypos = 0


def house():

    tt.pd()
    
    tt.speed(5)
    tt.hideturtle()
    tt.width(3)
   
    # bottom of house
    tt.fillcolor("green")
    tt.begin_fill()
    
    tt.forward(100)          
    tt.right(90)             
    tt.forward(100)          
    tt.right(90)             
    tt.forward(100)          
    tt.right(90)             
    tt.forward(100) 
         
    tt.end_fill()


    #top of house
    tt.fillcolor("blue")
    tt.begin_fill()
    
    tt.right(90)
    tt.forward(100)          
    tt.right(-120)           
    tt.forward(100)          
    tt.right(-120)           
    tt.forward(100)          
    tt.right(-120) 
    
    tt.end_fill()
    tt.pu() 
    
    
    #circle suns
    tt.goto(-100,50)
    tt.pd()
    tt.fillcolor("yellow")
    tt.begin_fill()
    r = 20
    n = 5
    for i in range(1, n + 1, 1): 
        tt.circle(r * i) 
    tt.end_fill()   
    tt.pu()
           

def main():
    
    house()
    
    turtle.exitonclick()
    turtle.bye()
    turtle.done()
    
main()


























