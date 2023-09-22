from turtle import *#running everything in Turtle
from random import *#getting some random number generator

 #setting t as a variable for our turtle
shape('turtle')
pensize(2)
speed(10)

def buildredtriangle():
    pencolor("red")
    fillcolor("red")
    begin_fill()
    for _ in range(2):
        forward(100)
        rt(120)
    end_fill()

def buildcircle():
    for _ in range(360):
        forward(1)
        rt(1)

def buildsquare():
    for _ in range(4):
        forward(100)
        rt(90)

def randommove():
    rand_forward = randrange(25, 300)
    rand_left_turn = randrange(45, 180)
    forward(rand_forward)
    lt(rand_left_turn)

buildredtriangle()
randommove()
buildsquare()



mainloop()