from turtle import *#running everything in Turtle
from sys import *

def set_turtle():
    pensize(4)
    speed(10)
    color("blue")

'''This is a list of colors for inspiration: yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, 
skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white'''

def build_triangle(size, color): #making a randomly generated Triangle of different sizes and colors
    pencolor(color)
    fillcolor(color)
    begin_fill()
    lt(180)
    for _ in range(2):
        forward(size)
        rt(120)
    end_fill()


def build_circle(size, color): #making a specific size of circle with a choice of color
    pencolor(color)
    fillcolor(color)
    begin_fill()
    circle(size)
    end_fill()


def build_rectangle(length, width, color): #making a specific size of rectangle with a choice of color
    pencolor(color)
    fillcolor(color)
    begin_fill()
    for _ in range(2):
        forward(length)
        lt(90)
        forward(width)
        lt(90)
    end_fill()

def build_house(location, size, color, color2):
    if size > 0:
        penup()
        goto(location, 0)
        pendown()
        build_rectangle(size, size, color)
        penup()
        goto(location + size*1.1, size*1.03)
        pendown()
        build_triangle(size*1.2, color)
        penup()
        goto(location + size*0.85, size*0.85)
        pendown()
        setheading(180)
        build_rectangle(size/4, size/4, color2)
        penup()
        goto(location + size*0.15, size*0.85)
        setheading(270)
        pendown()
        build_rectangle(size/4, size/4, color2)
        penup()
        goto(location+ size*0.375, 0)
        pendown()
        setheading(0)
        build_rectangle(size/4, size*0.4, color2)
    if size < 0:
        penup()
        goto(location + size, 0)
        pendown()
        build_rectangle(size, -size, color)
        penup()
        goto(location + size*0.9, -size*1.03)
        pendown()
        build_triangle(-size*1.2, color)
        penup()
        goto(location + size*1.15, -size*0.85)
        pendown()
        setheading(90)
        build_rectangle(size/4, -size/4, color2)
        penup()
        goto(location + size*1.85, -size*0.85)
        setheading(180)
        pendown()
        build_rectangle(size/4, -size/4, color2)
        penup()
        goto(location  + size*1.375, 0)
        pendown()
        setheading(0)
        build_rectangle(size/4, -size*0.4, color2)


    
def build_sun(location, size, color, color2, color3):
    penup()
    goto(location, 200)
    pendown()
    build_circle(size, color)
    penup()
    goto(location, 200 + size/2)
    pendown()
    build_circle(size/2, color2)
    penup()
    goto(location - size, 200 + size *1.5)
    setheading(90)
    pendown()
    build_triangle(size, color3)
    penup()
    goto(location + size, 200 + size *0.5)
    setheading(270)
    pendown()
    build_triangle(size, color3)
    penup()
    

def main(x):
    if x == 1: #Halloween
        set_turtle()
        build_house(150, 50, "purple", "gold")
        build_house(-150, 50, "gold", "purple")
        build_house(50, 50, "Black", "Orange")
        build_house(-50, 50, "orange", "black")
        build_sun(150, 50, "black", "orange", "red")
    elif x == 2: #Christmas
        set_turtle()
        build_house(150, 100, "green", "red")
        build_house(-150, 100, "red", "green")
        build_sun(200, 40, "blue", "skyblue", "red")
    elif x == 3: #valentines
        set_turtle()
        build_house(50, 100, "pink", "blue")
        build_house(-50, 100, "blue", "pink")
        build_house(250, 150, "red", "pink")
        build_sun(-100, 75, "pink", "red", "blue")
    else:
        print("Please input 1, 2, or 3")

print(argv[1])
main(int(argv[1]))


