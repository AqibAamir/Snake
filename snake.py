import turtle
import random
import time

# Create a screen
screen = turtle.Screen()
screen.title("WELCOME TO THE SNAKE GAME")
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("#32CD32")

# Creating the border for the environment
turtle.speed(6)
turtle.pensize(5)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("black")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Score display
score = 0
delay = 0.1

# Snake body
snake = turtle.Turtle()
snake.speed()
snake.shape("triangle")
snake.color("blue")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Function to set the snake's orientation
def set_snake_orientation():
    if snake.direction == "up":
        snake.setheading(90)
    elif snake.direction == "down":
        snake.setheading(270)
    elif snake.direction == "left":
        snake.setheading(180)
    elif snake.direction == "right":
        snake.setheading(0)

# Food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("circle")
fruit.color("brown")
fruit.penup()
fruit.goto(30, 30)

ancient_fruit = []

# Scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("black")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Your Score is:  ", align="center", font=("Courier", 24, "bold"))


# Define how to move
def snake_go_up():
    if snake.direction != "down":
        snake.direction = "up"


def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"


def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"


def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"


def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)


