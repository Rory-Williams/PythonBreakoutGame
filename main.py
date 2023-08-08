from turtle import Screen
import time
from breaker_bat import Bat
from ball import Ball
from score import Score
from bricks import Bricks

WIDTH = 600
BAT_WIDTH = 3
BAT_Y_POS = -250
SCREEN_TOP = 220
screen = Screen()
screen.setup(width=WIDTH, height=600)
screen.bgcolor('black')
screen.title('Breaker Game')
screen.tracer(0)

bat = Bat(WIDTH, BAT_WIDTH, BAT_Y_POS)
bricks = Bricks(WIDTH, SCREEN_TOP)
ball = Ball(WIDTH, SCREEN_TOP)
score = Score()
speed = 0.07

screen.listen()
screen.onkey(bat.left, 'Left')
screen.onkey(bat.right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(speed)
    ball.move()


    # Check if bat-ball collision occurs
    if bat.xcor()-BAT_WIDTH*10 <= ball.xcor() <= bat.xcor()+BAT_WIDTH*10 and \
            BAT_Y_POS <= ball.ycor() <= BAT_Y_POS + 10:
        ball.bat_bounce() # changes y dir
        print('bounced')

    # Check for block collisions
    brick_collision = bricks.brick_hit(ball.xcor(),ball.ycor())
    if brick_collision:
        ball.bounce_y()
        score.update_score()

    if ball.ycor() < BAT_Y_POS - 40:
        print('ball out of bounds')
        score.game_over()
        time.sleep(1)
        score.reset()
        bricks.create_bricks()
        ball.hideturtle()
        ball = Ball(WIDTH, SCREEN_TOP)

screen.exitonclick()





