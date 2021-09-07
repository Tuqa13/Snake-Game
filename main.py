from turtle import Screen
import time
from Snake import Snake
from food import Food
from ScoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE SNAKE")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    for i in snake.segment:
        if (i != snake.head) and i.distance(food) < 20:
            food.change_position()
    if snake.head.distance(food) < 15:
        food.change_position()
        snake.extend()
        score.increment()

    # Detect collision with the wall
    if snake.head.xcor() > float(290) or snake.head.xcor() < float(-290) or\
            snake.head.ycor() > float(290) or snake.head.ycor() < float(-290):
        game_is_on = False
        score.game_over()

    # Detect collision with your tail
    for segment in snake.segment:
        if segment == snake.head:
            continue
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()





screen.exitonclick()
