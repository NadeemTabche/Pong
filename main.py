# import necessary modules
import turtle as t
import os
#Color settings
askuserPColor = str(input('Hi, please enter paddle color '))
askuserTcolor = str(input('please enter text color '))
askuserBcolor = str(input('please enter ball color '))

#difficulty mode + game loop
askuser = str(input("Choose one of the following gamemodes: easy, medium, or hard? "))
if askuser == "easy":
    PaddleSize = 5
    BallSpeed = 1

elif askuser == 'medium':
    PaddleSize = 4
    BallSpeed  = 1.4

elif askuser == 'hard':
    PaddleSize = 3
    BallSpeed = 1.7

else:
    print("erroneous input, try again")
    exit()
# defining player score variables
playerOneScore = 0
playerTwoScore = 0

# setting up window display features
window = t.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# creating left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color(askuserPColor)
leftpaddle.shapesize(stretch_wid=PaddleSize, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# creating right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color(askuserPColor)
rightpaddle.shapesize(stretch_wid=PaddleSize, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# creating ball
ball = t.Turtle()
ball.speed(BallSpeed)
ball.shape("circle")
ball.color(askuserBcolor)
ball.penup()
# ball spawn point and direction
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2

# creating pen for scorecard update
pen = t.Turtle()
pen.speed(1.4)
pen.color(askuserTcolor)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=("Arial", 24, "normal"))


# Moving the left paddle down
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)


# Moving the left paddle down
def leftpaddledown():
    y = leftpaddle.ycor()
    y = y - 90
    leftpaddle.sety(y)


# Moving the right paddle up
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)


# Moving right paddle down
def rightpaddledown():
    y = rightpaddle.ycor()
    y = y - 90
    rightpaddle.sety(y)


# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, "w")
window.onkeypress(leftpaddledown, "s")
window.onkeypress(rightpaddleup, "Up")
window.onkeypress(rightpaddledown, "Down")

# main game loop
while True:
    window.update()  # This method is mandatory to run the game

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # setting up the border
    if ball.ycor() > 290:  # Right top paddle Border
        ball.sety(290)
        ballydirection = ballydirection * -1

    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:  # right width paddle Border
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerOneScore = playerOneScore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerOneScore, playerTwoScore),
                  align="center", font=('Monaco', 24, "normal"))

    if (ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerTwoScore = playerTwoScore + 1
        pen.clear()
        pen.write("Player A: {}               Player B: {} ".format(playerOneScore, playerTwoScore),
                  align="center", font=('Monaco', 24, "normal"))

    # handling the collisions:
    # x coordinate limits
    if (ball.xcor() > 340) and (ball.xcor() < 350):
        # y coordinate limits
        if (ball.ycor() < rightpaddle.ycor() + 40) and ((ball.ycor() > rightpaddle.ycor() - 40)):
            ball.setx(340)
            ballxdirection = ballxdirection * -1

    # x coordinate limits
    if (ball.xcor() < -340) and (ball.xcor() > -350):
        # y coordinate limits
        if ((ball.ycor() < leftpaddle.ycor() + 40) and (ball.ycor() > leftpaddle.ycor() - 40)):
            ball.setx(-340)
            ballxdirection = ballxdirection * -1
