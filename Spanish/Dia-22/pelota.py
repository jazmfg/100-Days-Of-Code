from turtle import Turtle

class Pelota(Turtle):

    VELOCIDADES_POR_NIVEL = {
        1: 0.035,
        2: 0.025,
        3: 0.015
    }

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.mov_x = 4
        self.mov_y = 4
        self.velocidad = self.VELOCIDADES_POR_NIVEL[1]

    def mover(self):
        self.goto(self.xcor() + self.mov_x, self.ycor() + self.mov_y)

    def rebotar_y(self):
        self.mov_y *= -1

    def rebotar_x(self):
        self.mov_x *= -1

    def reiniciar(self):
        self.goto(0, 0)
        self.rebotar_x()

    def actualizar_velocidad(self, nivel):
        self.velocidad = self.VELOCIDADES_POR_NIVEL[nivel]