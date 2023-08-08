from turtle import Turtle
import numpy as np

MOVE_DIST = 20
BODY_SEP = 20
RIGHT = 0
LEFT = 180
NUM_BRICK_COL = 10
NUM_BRICK_ROW = 4
PX_PADDING = 10
# BAT_WIDTH = 3

class Bricks():
    def __init__(self, width, screen_top):
        # self.goto(0, bat_y_pos)
        self.screen_width = width
        self.screen_top = screen_top
        self.brick_width = (width - (2+NUM_BRICK_COL)*PX_PADDING) // NUM_BRICK_COL
        print(self.brick_width)
        self.brick_y_coords = np.array([self.screen_top - 10 - 30 * x for x in range(NUM_BRICK_ROW)])
        self.brick_x_coords = np.array(range(-self.screen_width//2 + PX_PADDING + self.brick_width//2,
                                    self.screen_width//2 - PX_PADDING - self.brick_width//2,
                                    self.brick_width + PX_PADDING))
        print(self.brick_x_coords)
        print(self.brick_y_coords)
        self.create_bricks()


    def create_bricks(self):
        self.hit_bricks = []
        self.bricks = []
        pos = [0,0]
        for row in range(NUM_BRICK_ROW):
            for col in range(NUM_BRICK_COL):
                # print(col)
                pos[0] = self.brick_x_coords[col]
                pos[1] = self.brick_y_coords[row]
                self.add_seg(pos)


    def add_seg(self, position):
        seg = Turtle(shape='square')
        seg.shapesize(0.8, self.brick_width/20)
        seg.color('white')
        seg.pu()
        seg.setheading(180)
        seg.goto(position[0], position[1])
        self.bricks.append(seg)


    def brick_hit(self, ball_x, ball_y):
        y_dist = abs(self.brick_y_coords - ball_y)
        x_dist = abs(self.brick_x_coords - ball_x)
        y_check = np.nonzero(y_dist<10)
        x_check = np.nonzero(x_dist<self.brick_width/2)
        if y_check[0].size != 0:
            if x_check[0].size != 0:
                # print('hit')
                print(x_check)
                seg_location = y_check[0][0] * NUM_BRICK_COL + x_check[0][0]
                if seg_location not in self.hit_bricks:
                    self.hit_bricks.append(seg_location)
                    print(seg_location)
                    self.bricks[seg_location].color('black')
                    return True



