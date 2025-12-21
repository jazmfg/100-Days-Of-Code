import random
from turtle import Turtle

class Comida(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refrescar()

    def refrescar(self):
        x_aleatorio = random.randint(-280, 280)
        y_aleatorio = random.randint(-280, 280)
        self.goto(x_aleatorio, y_aleatorio)