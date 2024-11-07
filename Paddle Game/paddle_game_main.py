from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.tracer(0)
scoreboard=Scoreboard()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Paddle Game")
left_paddle=Paddle((-350,0))
right_paddle=Paddle((350,0))
screen.listen()
screen.onkey(left_paddle.up,"w")
screen.onkey(left_paddle.down,"s")
screen.onkey(right_paddle.up,"Up")
screen.onkey(right_paddle.down,"Down")
ball=Ball()
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(right_paddle) < 50 and ball.xcor()>320 or ball.distance(left_paddle) < 50 and ball.xcor()<-320:
        ball.x_bounce()
    if ball.xcor()> 400:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor()< -400:
        ball.reset_position()
        scoreboard.r_point()



screen.exitonclick()



