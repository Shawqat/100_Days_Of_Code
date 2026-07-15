from turtle import Turtle, Screen
import random

# colours = ["red","green","blue"]
my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("green")

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    return (red,green,blue)

# for i in range(50):
#     my_turtle.forward(10*i)
#     my_turtle.penup() 
#     my_turtle.forward(i)
#     my_turtle.pendown()
#     my_turtle.right(90)
#     my_turtle.color(random.choice(colours))

for _ in range(10):
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.color(random_color())


# tuple : immutable data type, we can't edit or remove it's items once created
# my_tuple = (1, 2, 3)
# print(my_turtle[0])



screen = Screen()
# to not hidden till i clicked
screen.exitonclick()