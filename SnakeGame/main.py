from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)  # pauses screen

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.onkey(key='Up', fun=snake.move_up)
screen.onkey(key='Down', fun=snake.move_down)
screen.onkey(key='Left', fun=snake.move_left)
screen.onkey(key='Right', fun=snake.move_right)
screen.listen()

game_on: bool = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        food.spawn()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        #game_on = False

    #Detect collision with tail
    for segment in snake.segments[1:]: #everything after [0]
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            #game_on = False

screen.exitonclick()
