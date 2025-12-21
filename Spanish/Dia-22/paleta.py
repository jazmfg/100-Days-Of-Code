from turtle import Turtle

class Paleta(Turtle):

    def __init__(self, posicion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(posicion)

    def subir(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor() + 20)

    def bajar(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor() - 20)