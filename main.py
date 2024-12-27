import turtle
playerAscore = 0
playerBscore = 0

wn = turtle.Screen()
wn.title("Ping pong game")
wn.bgcolor("black")
wn.setup(width= 800, height= 620)
wn.tracer(0)

# blocker 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# blocker 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
# ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape('circle')
ball.color('red')
ball.penup()
ball.goto(0,0)
ballxdirection=0.2
ballydirection=0.2
# pen2 to draw boundary
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('white')
pen2.penup()
pen2.hideturtle()
pen2.goto(0,240)
pen2.write("-----------------------------------------------------------------------", align='center', font=('Arial', 24, 'normal'))
pen2.goto(0,-290)
pen2.write('''|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
''', align='center', font=('Arial', 24, 'normal'))
pen2.goto(0,-310)
pen2.write("-----------------------------------------------------------------------", align='center', font=('Arial', 24, 'normal'))
# pen ;; for changing the scorecard
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 270)
pen.write("score", align='center',font=('Arial', 24, 'normal'))

# movement of left paddle
def leftpaddleup():
    y = paddle_1.ycor() ## This essentially sets the y cords of left paddle to be y, which can be used for manipulation
    y = y+40
    paddle_1.sety(y)

def leftpaddledown():
    y = paddle_1.ycor()
    y = y-40
    paddle_1.sety(y)

# moving the right paddle
def rightpaddleup():
    y = paddle_2.ycor()  ## This essentially sets the y cords of right paddle to be y, which can be used for manipulation
    y = y + 40
    paddle_2.sety(y)

def rightpaddledown():
    y = paddle_2.ycor()
    y = y-40
    paddle_2.sety(y)

# controls:
wn.listen()
wn.onkeypress(leftpaddleup, 'w')
wn.onkeypress(leftpaddledown, 's')
wn.onkeypress(rightpaddleup, 'Up')
wn.onkeypress(rightpaddledown, 'Down')
while True:
    wn.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    ## limiting how far the ball can go
    if ball.ycor() > 230:
        ball.sety(230)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1
    if paddle_1.ycor() >= 230:
        paddle_1.sety(230)
    if paddle_1.ycor() <= -270:
        paddle_1.sety(-270)
    if paddle_2.ycor() >= 230:
        paddle_2.sety(230)
    if paddle_2.ycor() <= -270:
        paddle_2.sety(-270)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerAscore = playerAscore + 1
        pen.clear()
        pen.write("Player A : {}               Player B : {}".format(playerAscore, playerBscore), align = 'center', font=('Arial', 24, 'normal'))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A : {}               Player B : {}".format(playerAscore, playerBscore), align = 'center', font=('Arial', 24, 'normal'))
    # dealing with collisions :
    if (ball.xcor() >340) and (ball.xcor()<350)and(ball.ycor()<paddle_2.ycor()+60 and ball.ycor()>paddle_2.ycor()-60):
        ball.setx(340)
        ballxdirection = ballxdirection * -1
    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor()<paddle_1.ycor()+60 and ball.ycor() > paddle_1.ycor()-60):
        ball.setx(-340)
        ballxdirection = ballxdirection * -1