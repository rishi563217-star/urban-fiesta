from turtle import Turtle,Screen
# from paddle import Paddle

paddle = Turtle(shape="square")
s = Screen()
s.bgcolor("black")
s.setup(width=800,height=678)
s.tracer(0)


paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)
# r_paddle(-350,0)
# l_paddle(350,0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

s.listen()
s.onkey(go_up,"Up")
s.onkey(go_down,"Down")

game_is_on=True
while game_is_on:
    s.update()


s.exitonclick()

