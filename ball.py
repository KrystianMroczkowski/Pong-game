from turtle import Turtle
from scoreboard import Scoreboard
POSITION = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1, 1)
        self.penup()
        self.goto(POSITION)
        self.direction_x = 10
        self.direction_y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.direction_x
        new_y = self.ycor() + self.direction_y
        self.goto(new_x, new_y)

    def wall_hit(self):
        if self.ycor() < -280:
            self.direction_y *= -1
        elif self.ycor() > 280:
            self.direction_y *= -1

    def paddle_hit(self, xcor_l, ycor_l, xcor_r, ycor_r):
        if self.xcor() > 0:
            if self.xcor() == xcor_r - 10 and ycor_r + 50 > self.ycor() > ycor_r - 50:
                self.direction_x = -10
                self.move_speed *= 0.9
        elif self.xcor() < 0:
            if self.xcor() == xcor_l + 10 and ycor_l + 50 > self.ycor() > ycor_l - 50:
                self.direction_x = 10
                self.move_speed *= 0.9

    def out_of_bounds(self, scoreboard):
        if self.xcor() > 380:
            self.goto(POSITION)
            self.move_speed = 0.1
            self.direction_x *= -1
            scoreboard.l_score += 1
            scoreboard.update_scoreboard()
        elif self.xcor() < -380:
            self.goto(POSITION)
            self.move_speed = 0.1
            self.direction_x *= -1
            scoreboard.r_score += 1
            scoreboard.update_scoreboard()

