import turtle
import time
import random

delay = 0.1  # Delay for the game loop

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


#snake food

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
 
segments = []  # List to hold the snake segments

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

    if head.distance(food) < 20:
        # Move the food to a random position
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        food.goto(x, y)
        #add a segment to the snake
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape("square")
        segment.color("grey")
        segment.penup()
        segments.append(segment) 
    #move the segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    
    #move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)


    move()  # Move the snake
    time.sleep(delay)  # Delay to control the speed of the game

window.mainloop()  # Keeps the window open