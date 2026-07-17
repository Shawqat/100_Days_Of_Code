from turtle import Turtle, Screen
import random

turtles = []
colours = ["red","green","blue","purple","black"]
screen = Screen()
user_prediction = screen.textinput(title = "make your prediction", prompt = "Wihch turtle will win the race, enter the color:(red,green,purple,yellow)")
screen.setup(width=500, height=400)

is_race_on = False

direction = 10

for turtle_index in range(5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=direction + (-100))
    turtles.append(new_turtle)
    direction += 40

def moving_forwards(t):
    t.forward(random.randint(1,12))


if user_prediction:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            if user_prediction == turtle.color()[0]:
                print("you predict it right! :D")
            else:
                print(f"sorry ur prediction is wrong\nThe turtle that won is : {turtle.color()[0]}")
            is_race_on = False
        else:
            moving_forwards(turtle)



screen.exitonclick()