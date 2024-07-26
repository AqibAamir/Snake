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

# Binding your keyboard
screen.listen()
screen.onkeypress(snake_go_up, "Up" )
screen.onkeypress(snake_go_up, "w" )
screen.onkeypress(snake_go_down, "Down" )
screen.onkeypress(snake_go_down, "s" )
screen.onkeypress(snake_go_left, "Left" )
screen.onkeypress(snake_go_left, "a" )
screen.onkeypress(snake_go_right, "Right" )
screen.onkeypress(snake_go_right, "d" )


# Game over function
def game_over():
    time.sleep(1)
    screen.clear()
    screen.bgcolor("salmon")
    scoring.goto(0, 0)
    scoring.write("GAME OVER \n Your score is {}".format(score), align="center", font=("Courier", 30, "bold"))
    screen.update()
    time.sleep(3)
    turtle.bye()


# Main loop
while True:
    screen.update()

    # Snake-fruit collision
    if snake.distance(fruit) < 20:
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # Increase score
        score += 1
        scoring.clear()
        scoring.write("Your Score is: {}".format(score), align="center", font=("Courier", 24, "bold"))

# Increase speed and create a new snake segment
        delay -= 0.001
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("circle")
        new_fruit.color("brown")
        new_fruit.penup()
        ancient_fruit.append(new_fruit)

    # Adding body
    for index in range(len(ancient_fruit) - 1, 0, -1):
        a = ancient_fruit[index - 1].xcor()
        b = ancient_fruit[index - 1].ycor()
        ancient_fruit[index].goto(a, b)

    if len(ancient_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        ancient_fruit[0].goto(a, b)

    snake_move()

    # Set snake orientation
    set_snake_orientation()

# Snake and border collision
    if (
        snake.xcor() > 280
        or snake.xcor() < -300
        or snake.ycor() > 240
        or snake.ycor() < -240
    ):
        game_over()

    # Snake self-collision
    for segment in ancient_fruit:
        if snake.distance(segment) < 20:
            game_over()

    time.sleep(delay)




