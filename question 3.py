# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:26:05 2020

@author: amand

"""
# Turtle Assignment
# Amanda Faulconer
# In a function draw a shape of your choosing except for the square. 
# Using recursion, draw multiples of that shape on the screen inwardly or 
# outwardly. 

import turtle

try:
    sc = turtle.Screen()
    tt = turtle.Turtle()
    
except:
    sc = turtle.Screen()
    tt = turtle.Turtle()
    
status = True

def window():
    sc.setup(750,750)

def recursiveTriangle(x,y, shrink):
    if x > -10:
        return
    
    tt.penup()
    tt.pensize(3) 
    tt.setx(x)
    tt.sety(y)
    tt.pendown()
    
    side = 2 * abs(x)
    
    for i in range(3):
        tt.forward(side)
        tt.left(120)
        
        
    recursiveTriangle(x + shrink, y + 0.5 * shrink, shrink)
    

def main():
    recursiveTriangle(-300,-250,30)
main()


































