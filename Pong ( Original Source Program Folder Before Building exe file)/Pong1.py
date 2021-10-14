#Getting started

import turtle
import winsound #For sound in Windows
import os       #For sound in Mac and Linux

wn = turtle.Screen()
wn.title("Pong by Masterverse")
wn.bgcolor("grey")
wn.setup(width=800, height=600)
wn.tracer(0)





# Score
score_a = 0
score_b = 0





# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)





# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)





# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)
ball.dx = .4
ball.dy = .4





# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "bold"))





# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y) 

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)      

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
    
    
    
    

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")

wn.listen()
wn.onkeypress(paddle_a_down, "s")

wn.listen()
wn.onkeypress(paddle_b_up, "Up")

wn.listen()
wn.onkeypress(paddle_b_down, "Down")





#Main game loop
while True:
    wn.update()
    
    
    
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    
    
    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        #os.system("aplay Boundary_hit.wav&") #For sound in Linux
        #os.system("afplay Boundary_hit.wav&") #For sound in Mac
        winsound.PlaySound("Boundary_hit.wav", winsound.SND_ASYNC) #For sound in Wondows
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        #os.system("aplay Boundary_hit.wav&") #For sound Linux
        #os.system("afplay Boundary_hit.wav&") #For sound in Mac
        winsound.PlaySound("Boundary_hit.wav", winsound.SND_ASYNC) #For sound in Wondows
        
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "bold"))
        #os.system("aplay Game_over.wav") #For sound Linux
        #os.system("afplay Game_over.wav") #For sound in Mac
        winsound.PlaySound("Game_over.wav", winsound.SND_ASYNC) #For sound in Wondows
        
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1 
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}" , align="center", font=("Courier", 24, "bold"))
        #os.system("aplay Game_over.wav") #For sound Linux
        #os.system("afplay Game_over.wav") #For sound in Mac
        winsound.PlaySound("Game_over.wav", winsound.SND_ASYNC) #For sound in Wondows
        
    if paddle_a.ycor() > 260:
        paddle_a.sety(260)   
        
    if paddle_a.ycor() < -260:
        paddle_a.sety(-260)   
        
    if paddle_b.ycor() > 260:
        paddle_b.sety(260)   
        
    if paddle_b.ycor() < -260:
        paddle_b.sety(-260)      
         
        
        
        
    # Paddle and ball collision
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1 
        #os.system("aplay Hit.wav&") #For sound in Linux
        #os.system("afplay Hit.wav&") #For sound in Mac
        winsound.PlaySound("Hit.wav", winsound.SND_ASYNC) #For sound in Wondows

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1   
        #os.system("aplay Hit.wav&") #For sound in Linux
        #os.system("afplay Hit.wav&") #For sound in Mac
        winsound.PlaySound("Hit.wav", winsound.SND_ASYNC) #For sound in Wondows
