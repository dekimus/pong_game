from turtle import Turtle
STEP = 20

class Paddle(Turtle):

    def __init__(self, pos) -> None:
        super().__init__()
        self.pos = pos
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((self.pos,0))
        self.shapesize(5,1)
        #self.setheading(90)


    def move_up(self):
        if self.ycor() < 240:
            nPos = self.ycor() + STEP
            self.goto((self.pos,nPos)) 
        #self.forward(STEP)

    def move_down(self):
        if self.ycor() > -240:
            nPos = self.ycor() - STEP
            self.goto((self.pos,nPos)) 
