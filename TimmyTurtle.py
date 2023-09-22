from turtle import *#running everything in Turtle
from random import *#getting some random number generator

 #setting t as a variable for our turtle
shape('turtle')
pensize(4)
speed(10)

'''yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, 
skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white'''

color_list = ["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", 
"skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", 
"chocolate", "brown", "black", "gray",]
ran_color = choice(color_list)
ran_size1 = randrange(30, 100)
ran_size2 = randrange(1,4)

def build_triangle(): #making a randomly generated Triangle of different sizes and colors
    ran_color = choice(color_list)
    ran_size1 = randrange(15, 125) 
    triangle_color = ran_color
    pencolor(triangle_color)
    fillcolor(triangle_color)
    if triangle_color == "gold" or triangle_color == "magenta":
        ran_size1 = 225
    begin_fill()
    for _ in range(2):
        forward(ran_size1)
        rt(120)
    end_fill()


def build_circle(): #making a randomly generated circle of different colors and sizes
    ran_color = choice(color_list)
    ran_size2 = randrange(15,80)
    circle_color = ran_color
    pencolor(circle_color)
    fillcolor(circle_color)
    if circle_color == "gold" or circle_color == "purple":
        ran_size2 = 115
    begin_fill()
    circle(ran_size2)
    end_fill()


def build_square(): #making a randomly generated square with different colors and sizes
    ran_color = choice(color_list)
    ran_size1 = randrange(15, 125)
    square_color = ran_color
    pencolor(square_color)
    fillcolor(square_color)
    if square_color == "purple" or square_color == "magenta":
        ran_size1 = 175
    begin_fill()
    for _ in range(4):
        forward(ran_size1)
        rt(90)
    end_fill()


def random_move():
    up()
    rand_x = randrange(-300, 300)
    rand_y = randrange(-300, 300)
    setx(rand_x)
    sety(rand_y)
    down()

shape_number = 0
shape_max = randrange(30, 60)

while (shape_number < shape_max): #the main running loop to make it continuously go until completed.
    build_triangle()
    shape_number += 1
    random_move()
    build_square()
    shape_number += 1
    random_move()
    build_circle()
    shape_number += 1
    random_move()


mainloop()