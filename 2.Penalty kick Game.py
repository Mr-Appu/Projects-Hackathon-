import turtle
from turtle import Turtle
import random
import time
turtle.hideturtle()
turtle.speed(0)

#screen
s=turtle.Screen()
s.title("GAME")
s.bgcolor("forestgreen")
s.setup(width=800,height=600)

#penalty kick
turtle.pencolor("yellow")
turtle.penup()
turtle.setpos(0,200)
turtle.write("PENALTY KICK",font=("Arial", 30, "bold"),align="center")


#Goal area
turtle.pen()
turtle.setpos(-350,-300)
turtle.fillcolor("white")
turtle.begin_fill()
for x in range(2):
    turtle.forward(700)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
turtle.end_fill()

#ball
turtle.setpos(0,0)
turtle.showturtle()
turtle.color("black")
turtle.shape("circle")
turtle.shapesize(2)
turtle.right(90)


#goal keeper
gk=Turtle()
gk.shape("square")
gk.shapesize(stretch_wid=1,stretch_len=3)
gk.speed(0)
gk.showturtle()
gk.penup()
gk.color("red")
gk.goto(0,-260)

#gk moving 
def move_right():
    x=gk.xcor()
    if x<320:
        gk.setx(x+40)
def move_left():
    x=gk.xcor()
    if x>-320:
        gk.setx(x-40)


s.listen()
s.onkeypress(move_right,"Right")
s.onkeypress(move_left,"Left")
time.sleep(1)

#ball moving
turtle.speed(1)
px=random.randrange(0,281,40)
x=random.randint(1,2)
if x==1:
    turtle.setposition(px,-238)
if x==2:
    turtle.setposition(-px,-238)

#game
if gk.xcor()==turtle.xcor():
    if x==2:
        turtle.right(120)
        turtle.forward(100)
    if x==1:
        turtle.left(120)
        turtle.forward(100)
    print("win")


    
