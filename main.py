from turtle import *

turtle=Turtle()
screen=Screen()

def forwards():
    turtle.forward(10)
    
def backwards():
    turtle.backward(10)
    
def left():
    turtle.left(10)
    
def right():
    turtle.right(10)    

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    


screen.listen()
screen.onkey(forwards,'w')
screen.onkey(left,'a')
screen.onkey(backwards,'s')
screen.onkey(right,'d')
screen.onkey(clear,"c")

screen.exitonclick()