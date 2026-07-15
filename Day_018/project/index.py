from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
# tim.pensize(15)
tim.speed("fastest")
colormode(255)
tim.hideturtle()


def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return (red,green,blue)

tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)

def draw_line():
    for _ in range(10):
        tim.dot(20,random_color())
        tim.penup()
        tim.forward(50)
        tim.pendown()

    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

for _ in range(10):
    draw_line()








screen = Screen()
screen.exitonclick()