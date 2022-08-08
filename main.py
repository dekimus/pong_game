from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#constantes
WIDTH = 800
HEIGHT = 600
POSI = -350
POSD = 350

#configuración de pantalla
sc = Screen()
sc.bgcolor("black")
sc.setup(WIDTH,HEIGHT)
sc.title("PONG!")
sc.tracer(0)
sc.listen()
#En juego
on= True

#los paddles
paddle_iz = Paddle(POSI)
paddle_de = Paddle(POSD)
sc.onkeypress(key="w", fun=paddle_iz.move_up)
sc.onkeypress(key="s", fun=paddle_iz.move_down)
sc.onkeypress(key="Up", fun=paddle_de.move_up)
sc.onkeypress(key="Down", fun=paddle_de.move_down)

#Pelota
ball = Ball()

#Scores
sb = ScoreBoard()


while on:
    time.sleep(0.01)
    sc.update()
    ball.move()

    if ball.ycor() > 290  or ball.ycor() < -290:
        ball.bounceY()
        
    if ball.distance(paddle_de) < 50 and ball.xcor()>320 or ball.distance(paddle_iz) < 50 and ball.xcor()<-320:
        ball.bounceX()

    if ball.xcor() < -380:
        sb.rscore()
        ball.reset_ball()

    if ball.xcor() > 380:
        sb.lscore()
        ball.reset_ball()
    

















sc.exitonclick()




















