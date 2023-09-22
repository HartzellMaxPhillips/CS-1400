import turtle #running everything in Turtle

t = turtle.Turtle #setting t as a variable for our turtle

def buildtriangle():
    for _ in range(3):
        t.forward(100)
        t.rt(120)

buildtriangle


turtle.mainloop()