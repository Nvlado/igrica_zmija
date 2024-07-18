from turtle import Turtle
import random

class Hrana(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.osvezi()

    def osvezi(self):
        x_osa = random.randint(-200, 200)
        y_osa = random.randint(-200, 200)
        self.goto(x_osa, y_osa)