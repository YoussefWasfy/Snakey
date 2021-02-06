from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 0
        self.highscore = int(float(self.read_highscore()))
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", align='center',
                   font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER!!", align='center', font=('Arial', 50, 'normal'))
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore(self.highscore)
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        with open('data.txt') as data:
            high_score = data.read()
        return high_score

    def write_highscore(self, high_score):
        with open('data.txt', mode='w') as data:
            data.write(str(high_score))
