from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,220)
        self.r_score = 0
        self.l_score = 0
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"{self.l_score}     {self.r_score}",align="CENTER", font=("Arial",60, "normal"))

    def lscore(self):
        self.l_score += 1
        self.update_score()
    
    def rscore(self):
       self.r_score += 1
       self.update_score()