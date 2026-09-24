import random
import turtle

# Screen setup
screen = turtle.Screen()
screen.title("Turtle Race 🐢🏁")
screen.bgcolor("white")
screen.setup(width=900, height=600)
screen.tracer(0)

# Race settings
START_X = -400
FINISH_X = 380
LANES = [150, 50, -50, -150]
COLORS = ["red", "blue", "green", "orange"]

# Draw finish line
finish_line = turtle.Turtle()
finish_line.hideturtle()
finish_line.penup()
finish_line.goto(FINISH_X, -220)
finish_line.setheading(90)
finish_line.pendown()
finish_line.pensize(4)
finish_line.color("black")
finish_line.forward(440)

# Draw lane lines
lane_marker = turtle.Turtle()
lane_marker.hideturtle()
lane_marker.penup()
lane_marker.color("lightgray")
for y in [100, 0, -100]:
    lane_marker.goto(START_X, y)
    lane_marker.setheading(0)
    lane_marker.pendown()
    lane_marker.forward(FINISH_X - START_X)
    lane_marker.penup()

# Create turtles
racers = []
for color, y in zip(COLORS, LANES):
    racer = turtle.Turtle(shape="turtle")
    racer.color(color)
    racer.penup()
    racer.goto(START_X, y)
    racer.setheading(0)
    racers.append(racer)

# Countdown
message = turtle.Turtle()
message.hideturtle()
message.penup()
message.goto(0, 220)
message.write("3", align="center", font=("Arial", 32, "bold"))
screen.update()
screen.ontimer(lambda: update_message("2"), 700)
screen.ontimer(lambda: update_message("1"), 1400)
screen.ontimer(lambda: update_message("GO!"), 2100)
screen.ontimer(lambda: start_race(), 2800)


def update_message(text):
    message.clear()
    message.write(text, align="center", font=("Arial", 32, "bold"))


def start_race():
    message.clear()
    race()


def race():
    for racer in racers:
        racer.forward(random.randint(1, 10))

    screen.update()

    for racer in racers:
        if racer.xcor() >= FINISH_X:
            winner = racer.pencolor()
            message.write(
                f"Winner: {winner.upper()} turtle! 🏆",
                align="center",
                font=("Arial", 24, "bold"),
            )
            return

    screen.ontimer(race, 50)


screen.mainloop()
