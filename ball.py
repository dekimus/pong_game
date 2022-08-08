from turtle import Turtle

VEL = 3

class Ball(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.m_x = VEL
        self.m_y = VEL

    def move(self):
        newy = self.ycor() + self.m_y
        newx = self.xcor() + self.m_x
        self.goto(newx, newy)

    def bounceY(self):
        self.m_y *= -1

    def bounceX(self):
        self.m_x *= -1
    
    def reset_ball(self):
        self.goto(0,0)
        self.bounceX()