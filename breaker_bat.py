from turtle import Turtle

MOVE_DIST = 20
BODY_SEP = 20
RIGHT = 0
LEFT = 180
# BAT_WIDTH = 3

class Bat(Turtle):
    def __init__(self, width, bat_width, bat_y_pos):
        super().__init__()
        self.goto(0, bat_y_pos)
        self.bat_width = bat_width
        self.shape('square')
        # self.bat = Turtle(shape='square')
        self.color('white')
        self.shapesize(0.8, bat_width)
        self.pu()
        self.bat_height = bat_y_pos
        self.reset()
        # self.heading = 90 #facing up
        self.setheading(180)
        self.screen_width = width
        print(self.screen_width)


    def reset(self):
        self.goto(0, self.bat_height)


    def left(self):
        if self.xcor() > (-self.screen_width + self.bat_width*20)/2:
            self.setheading(LEFT)
            self.forward(MOVE_DIST)


    def right(self):
        if self.xcor() < (self.screen_width - self.bat_width*20)/2:
            self.setheading(RIGHT)
            self.forward(MOVE_DIST)

