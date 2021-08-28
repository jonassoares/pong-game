from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=900, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((400, 0))
l_paddle = Paddle((-400, 0))

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # check wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check paddle collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 380 or ball.distance(l_paddle) < 50 and ball.xcor() < -380:
        ball.bounce_x()

    # score a point - left
    if ball.xcor() > 420:
        ball.reset_position()
        scoreboard.l_point()

    # score a point - right
    if ball.xcor() < -420:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
