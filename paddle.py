from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 30)

    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 30)
