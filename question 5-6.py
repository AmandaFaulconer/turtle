# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:46:20 2020

@author: amand
"""
# Turtle Assignment
# Amanda Faulconer
# 5. Animate a shape across the screen. If it goes off the screen have it 
#    appear from the other side.
#       -bounce the shape like animation 
#       -just make something move 

# 6. Animate a  gif of your choice.
#       -combined 5 & 6


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


def windowsetup():
    
    sc.setup(500,500)
    tt.speed(0)
    
    tt.width(3)
    sc.tracer(0)



def turtle_gif():
    
    tt.speed(0)
    sc.tracer(0)
    sc.addshape("turtle.gif")   
    
    tt.speed(0)
    tt.shape("turtle.gif")        
    tt.pu()
    
def animate_gif():
    
    global xpos, ypos
    global status
    
    dir = 1
    
    tt.pu()
    tt.goto(xpos,ypos)
    
    tt.pd()
    
    status = True
    
    while status:
        
        tt.clear()
        
        turtle_gif()
        
        sc.update()
        

        tt.forward(0.9 * dir)
        
        xpos = tt.xcor()
        ypos = tt.ycor()
        

        if(tt.xcor() >= 150 or tt.xcor() <= -250):
            dir = dir * -1


def main():
    
    
    windowsetup()
    
    turtle_gif()
    
    animate_gif()
    
    
    turtle.exitonclick()
    turtle.bye()
    turtle.done()
    
    
main()
