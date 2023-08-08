from turtle import Turtle
from random import randint
MOVE_DIST = 40
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# SCREEN_TOP = 220


class Ball(Turtle):
    def __init__(self, width, screen_top):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.y_dist = 10
        self.screen_width = width
        self.screen_top = screen_top
        print(f'width: {self.screen_width}')
        self.move_init()

    def move_init(self):
        # self.setheading(randint(1, 4) * 90 + 45)
        # self.x_move = 10 * (randint(0, 1) * 2 - 1)
        # self.y_move = self.y_dist * (randint(0, 1) * 2 - 1)
        self.x_move = 0
        self.y_move = -1 * self.y_dist

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        if self.screen_width/2 - 10 < new_x or new_x < -self.screen_width/2 + 10:
            self.bounce_x()
            new_x = self.xcor() + self.x_move
        if self.screen_top < new_y or new_y < -300:
            self.bounce_y()
            new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bat_bounce(self):
        self.bounce_y()
        xchange = randint(-15, 15)
        print(xchange)
        self.x_move += xchange

    def bounce_x(self):
        self.x_move *= -1






