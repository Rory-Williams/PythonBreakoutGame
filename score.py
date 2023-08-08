from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 32, 'normal')
COLOUR = 'white'

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 240)
        self.color(COLOUR)
        with open('Hiscore.txt', 'r') as hiscore:
            self.highscore = int(hiscore.read())
        self.score = 0
        self.write(f'Score: {self.score} Hiscore: {self.highscore}', align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} Hiscore: {self.highscore}', align=ALIGN, font=FONT)

    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score} Hiscore: {self.highscore}', align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGN, font=FONT)

    def reset(self):
        self.goto(0, 240)
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Hiscore.txt', 'w') as hiscore:
                hiscore.write(str(self.highscore))
        self.score = 0
        self.print_score()
