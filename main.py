from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

POSITION_R = (350, 0)
POSITION_L = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle_r = Paddle(POSITION_R)
paddle_l = Paddle(POSITION_L)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.wall_hit()
    ball.paddle_hit(paddle_l.xcor(), paddle_l.ycor(), paddle_r.xcor(), paddle_r.ycor())
    ball.out_of_bounds(scoreboard)
screen.exitonclick()