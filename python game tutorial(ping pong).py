"""
    Ping Pong Game
        - window setup
        - add game objects to the screen (paddles and ball)
        - moving the paddles 
        - moving the ball
        - logic
        - score
        - sounds
"""

import turtle
import winsound
import os

# window setup

wn = turtle.Screen()
wn.title('Ping Pong Game')
wn.bgcolor("black")
wn.setup(width=800 , height=600)

# wn.tracer(0)




# Add game objects to screen (paddles and ball)

paddle_a = turtle.Turtle()

paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color('blue')
paddle_a.penup()
paddle_a.goto(-350,0)


paddle_b = turtle.Turtle()

paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color('red')
paddle_b.penup()
paddle_b.goto(350,0)


ball = turtle.Turtle()

ball.speed(0)
ball.shape("square")
ball.color('white')
ball.penup()
ball.goto(0,0)

ball.dx = 0.15
ball.dy = 0.15


# Score

score_a = 0
score_b = 0 
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A:0 Player B:0 " , align="center" , font=("Courier" , 20 , "normal"))


# moving the paddle_a
def paddle_a_move_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y) 


def paddle_a_move_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)




# moving the paddle_b
def paddle_b_move_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y) 


def paddle_b_move_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_move_up,"w")
wn.onkeypress(paddle_a_move_down,"s")
wn.onkeypress(paddle_b_move_up,"Up")
wn.onkeypress(paddle_b_move_down,"Down")



while True :
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290 :
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_a +=1
        score.clear()
        score.write(f"Player A:{score_a} Player B:{score_b}" , align="center" ,font=("Courier" , 20 , "normal"))


    if ball.xcor() < -390 :
        ball.goto(0,0)
        ball.dx *= -1
        score_b +=1
        score.clear()
        score.write(f"Player A:{score_a} Player B:{score_b}" , align="center" ,font=("Courier" , 20 , "normal"))

    # paddle and ball collision

    if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40) :
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    if (ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40) :
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
