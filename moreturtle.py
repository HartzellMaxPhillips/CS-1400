import turtle

t = turtle.Turtle()
t.color('blue')
t.shape('turtle')
t.pensize(2)
t.speed(10)

def turn_right():
  t.rt(90)

def make_a_spiral():
    i = 4
    e = 0
    while e < 61:
        turn_right()
        t.forward(i)
        i = i + 4
        e = e + 1

def make_a_circle():
   c = 0
   while c < 360:
      t.forward(2)
      t.rt(1)
      c = c+1

def make_a_knot():
   c = 0
   while c < 4:
      t.forward(150)
      smallKnot = 0
      c = c+1
      while smallKnot < 3:
        t.forward(35)
        turn_right()
        smallKnot = smallKnot+1




turtle.mainloop()      # should be last line of program

'''
    t.forward(10) - Takes a number for the distance traveled
    t.backward(10) - Takes a number for the distance traveled
    t.rt(45) - Takes a number for degrees turned
    t.lt(45) - Takes a number for degrees turned
    t.color('red') - Takes a string for the color
    t.shape('turtle') - Takes one of the following strings 'turtle', 'circle', 'square', 'arrow', 'classic', or 'triangle'.
    t.pensize(4) - Takes a positive number
    t.speed(1) - Takes a number in the range 0..10
'''