# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:27:33 2020

@author: amand
"""
# Amanda Faulconer
# Turtle assignment
# Question 4
# In a function, draw a shape or shapes of your choosing. 
# Spiral the shape(s).  Try to change the color as it is draw.


import turtle


try:
    sc = turtle.Screen()
    tt = turtle.Turtle()
    
except:
    sc = turtle.Screen()
    tt = turtle.Turtle()

status = True

def spiral():
    
    tt.pencolor('hot pink')
    tt.width(3)
    tt.shape = 0
    tt.up()
    tt.speed(0)
    
    tt.right(50)
    tt.forward(200)          
    tt.right(-100)           
    tt.forward(200)          
    tt.right(-100)           
    tt.forward(200)          
    tt.right(-100)



    tt.pd() 
    while tt.shape < 120: 
        tt.fd(100)     
        tt.rt(90)
        tt.fd(100)
        tt.rt(90)
        tt.fd(100)
        tt.rt(90)
        tt.fd(100)
        tt.rt(90)

    
        tt.rt(15.2222) 
        tt.shape = tt.shape + 1 
    tt.pu()    
    tt.setpos(0,0)
    
        

        

def main():
    
    spiral()
   
    
    turtle.exitonclick()
    turtle.bye()
    turtle.done()
    
main()
  
  












