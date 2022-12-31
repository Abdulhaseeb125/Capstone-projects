import time
from Snake import *
from food import *
from score import *



def up():
    for i in snake.snake_list:
        if i.heading() != 270:
            i.setheading(90)


def down():
    for i in snake.snake_list:
        if i.heading() != 90:
            i.setheading(270)


def left():
    for i in snake.snake_list:
        if i.heading() != 0:
            i.setheading(180)


def right():
    for i in snake.snake_list:
        if i.heading() != 180:
            i.setheading(0)


snake = Snake()
food = Food()
score = Score()
snake.add_snake()



snake.screen.listen()
snake.screen.onkey(key="Up", fun=up)
snake.screen.onkey(key="Down", fun=down)
snake.screen.onkey(key="Left", fun=left)
snake.screen.onkey(key="Right", fun=right)
End = True
while End:
    snake.move()
    if snake.snake_list[0].distance(food) < 10:
        snake.extend()
        score.clear()
        score.Refresh()
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
    if snake.snake_list[0].xcor() > 290 or snake.snake_list[0].xcor() < -290 or snake.snake_list[0].ycor() > 290 or \
            snake.snake_list[0].ycor() < -290:
        for i in snake.snake_list:
            i.hideturtle()
        time.sleep(3)
        food.hideturtle()
        score.game_over()
        End = False
    time.sleep(0.05)
    snake.screen.update()

snake.screen.exitonclick()
