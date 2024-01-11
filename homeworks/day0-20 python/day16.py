#hw1
from turtle import *
def x():
    for i in range(4):
        forward(200)
        left(90)
def y():
    for i in range(3):
        forward(40)
        right(90)
def z():
    for i in range(2):
        right(90)
        forward(120)
        right(90)
        forward(60)
#we want to paint the house

#step 1:draw a square
speed(10)
width(7)
color("purple")
x()
#end of the square
#drawing a door
begin_fill()
forward(70)
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120) #height of the door
penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing the first window
penup()
goto(20, 140)
pendown()
color("yellow")
begin_fill()
right(150)
y()
forward(40)
end_fill()
#drawing the second window
penup()
goto(180, 140)
pendown()
begin_fill()
y()
forward(40)
right(90)
forward(40)
end_fill()
#painting the door
penup()
goto(70, 0)
color("green")
begin_fill()
z()
end_fill()

exitonclick()
#hw2
def square():
    f = input("insert size of the square's side to calculate its perimeter and area: ")
    print("perimeter of the square is " + str(int(f)*4))
    print("area of the square is " + str(int(f)**2))
square()
#hw3
def triangle():
    h = input("insert side of the triangle to calculate its perimeter: ")
    g = input("insert size of th second side: ")
    k = input("insert side of the third side: ")
    print("perimeter is " + str(int(h)+int(g)+int(k)))
triangle()
#hw4
p = 99
while p > 0:
    print(str(p) + "bottles of beer on the wall," + str(p) + "bottles of beer.Take one down and pass it around," + str(p-1) + "bottles of beer on the wall.")
    p = p - 1
print("No more bottles of beer on the wall, no more bottles of beer.Go to the store and buy some more, 99 bottles of beer on the wall.")