from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()


game_is_on=True
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    # detects collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend_snake()
        score.increase_scoreboard()

    # detects collision with wall

    if snake.head.xcor()> 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor()< -280:
        game_is_on=False
        score.game_over()

    # detects collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <10:
            game_is_on=False
            score.game_over()



screen.exitonclick()











screen.exitonclick()
