# Import required library
import turtle


# Create screen
sc = turtle.Screen()
sc.title("Pong game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)



# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)


# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)


# Initialize the score
left_player = 0
right_player = 0


# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(-100, 260)
sketch.write("0", align="center", font=("Courier", 32, "normal"))
sketch.goto(100, 260)
sketch.write("0", align="center", font=("Courier", 32, "normal"))

# Displays Vertical Line
sketch.width(5)
sketch.color("grey")
sketch.goto(0, 300)
sketch.right(90)
sketch.pendown()
for i in range(12):
	sketch.forward(25)
	sketch.penup()
	sketch.forward(25)
	sketch.pendown()

# Ball of circle shape
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(0, 0)


# Functions to move paddle vertically
def left_paddle_up():
	y = left_pad.ycor()
	y += 20
	left_pad.sety(y)


def left_paddle_down():
	y = left_pad.ycor()
	y -= 20
	left_pad.sety(y)


def right_paddle_up():
	y = right_pad.ycor()
	y += 20
	right_pad.sety(y)


def right_paddle_down():
	y = right_pad.ycor()
	y -= 20
	right_pad.sety(y)


# Keyboard bindings
sc.listen()
sc.onkeypress(left_paddle_up, "w")
sc.onkeypress(left_paddle_down, "s")
sc.onkeypress(right_paddle_up, "Up")
sc.onkeypress(right_paddle_down, "Down")


while True:
	sc.update()
