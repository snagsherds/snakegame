import turtle
import time

delay = 0.3  # Delay for the game loop

# set up the screen
window = turtle.Screen()
window.title("Rohans Snake Game")
window.bgcolor("black")
window.setup(width=500, height=500)
window.tracer(0)  # Turns off the screen updates for better performance

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "up"  # Initial direction of the snake

# Functions
def go_up():
    head.direction = "up"
def go_down():
    head.direction = "down"
def go_left():
    head.direction = "left"
def go_right():
    head.direction = "right"

# keybaindings
window.listen()  # Listen for keyboard input
window.onkeypress(go_up, "Up")      # Move up with Up arrow /w
window.onkeypress(go_down, "Down")  # Move down with Down arrow /s
window.onkeypress(go_left, "Left")  # Move left with Left arrow /a
window.onkeypress(go_right, "Right")# Move right with Right arrow /d

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#Main game Loop
while True:
    window.update()  # Update the screen
    move()  # Move the snake
    time.sleep(delay)  # Delay to control the speed of the game

window.mainloop()  # Keeps the window open