import turtle
import time
import random

delay = 0.15  # Delay for the game loop

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

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square") 
pen.color("white")
pen.penup()
pen.hideturtle()  # Hide the pen turtle
pen.goto(0, 210)  # Position the pen at the top
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))  # Initial score display

# Functions
def go_up():
    if head.direction != "down":  # Prevent the snake from going back on itself
        head.direction = "up"
def go_down():
    if head.direction != "up":  # Prevent the snake from going back on itself
        head.direction = "down"
def go_left():
    if head.direction != "right":  # Prevent the snake from going back on itself
        head.direction = "left"
def go_right():
    if head.direction != "left":  # Prevent the snake from going back on itself
        head.direction = "right"

# keybaindings
window.listen()  # Listen for keyboard input
window.onkeypress(go_up, "Up")      # Move up with Up arrow /w
window.onkeypress(go_down, "Down")  # Move down with Down arrow /s
window.onkeypress(go_left, "Left")  # Move left with Left arrow /a
window.onkeypress(go_right, "Right")# Move right with Right arrow /d


#Score
score = 0
high_score = 0




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

    # Check for collision with the border
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        head.goto(0, 0)  # Reset the snake to the center
        head.direction = "stop"  # Reset direction
        # Hide all segments
        for segment in segments:
            segment.goto(1000, 1000)  # Move off-screen
         # Clear the list of segments
        segments.clear()

        #reset score
        score = 0
        pen.clear()  # Clear the previous score display
        pen.write(f"Score: {score}    High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Update the score display



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

        #Shorthen the delay
        delay -= 0.001  # Decrease the delay to speed up the game

        #Increase the score
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()  # Clear the previous score display    
        pen.write(f"Score: {score}    High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Update the score display

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


    move()  # Move the 
    
    #CHECK FOR HEAD COLLISION WITH THE BODY
    for segment in segments:
        if segment.distance(head) < 20:
            head.goto(0, 0)  # Reset the snake to the center
            head.direction = "stop"  # Reset direction
            # Hide all segments
            for segment in segments:
                segment.goto(1000, 1000)  # Move off-screen
            segments.clear()  # Clear the list of segments

            # Reset score
            score = 0
            #Resert delay
            delay = 0.15  # Reset the delay to the initial value

            pen.clear()  # Clear the previous score display    
            pen.write(f"Score: {score}    High Score: {high_score}", align="center", font=("Courier", 24, "normal"))  # Update the score display
    time.sleep(delay)  # Delay to control the speed of the game

window.mainloop()  # Keeps the window open