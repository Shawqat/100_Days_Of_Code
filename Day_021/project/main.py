from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
# create snake body
snake = Snake()

# create random food on the screen
food = Food()

# board
board = Scoreboard()

# which direction to move
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")

# moving snake
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # The Eating process
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()
        
    # detect the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        board.game_over()
        game_is_on = False

    # detect the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            board.game_over()

screen.exitonclick()