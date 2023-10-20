from turtle import *#running everything in Turtle


def set_turtle():
    shape('turtle')
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

def build_house(size, color, color2):
    build_rectangle(size, size, color)
    penup()
    goto(size*1.1, size*1.03)
    pendown()
    build_triangle(size*1.2, color)
    penup()
    goto(size*0.85, size*0.85)
    pendown()
    setheading(180)
    build_rectangle(size/4, size/4, color2)
    penup()
    goto(size*0.15, size*0.85)
    setheading(270)
    pendown()
    build_rectangle(size/4, size/4, color2)
    penup()
    goto(size*0.375, 0)
    pendown()
    setheading(0)
    build_rectangle(size/4, size*0.4, color2)


    
def build_something():
    build_circle(50)

#def main()
set_turtle()
build_house(100, "purple", "gold")

'''while (shape_number < shape_max): #the main running loop to make it continuously go until completed.
    build_triangle()
    shape_number += 1
    random_move()
    build_square()
    shape_number += 1
    random_move()'''


mainloop()