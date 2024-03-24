from turtle import *

shape_input = input("Triangle, rectangle or square: ")

# setup pen
pensize(15)
shape("turtle")
pencolor("black")
fillcolor("blue")

# triangle
if(shape_input == "triangle"):
    begin_fill()
    right(120)
    forward(100)
    right(120)
    forward(100)
    right(120)
    forward(100)
    end_fill()
elif (shape_input == "rectangle"):
    begin_fill()
    right(90)
    forward(200)
    right(90)
    forward(100)
    right(90)
    forward(200)
    right(90)
    forward(100)
    end_fill()
elif (shape_input == "square"):
    begin_fill()
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    end_fill()

mainloop()