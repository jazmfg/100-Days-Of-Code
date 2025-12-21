from turtle import Turtle

POSICION_INICIAL = (0, -280)
DISTANCIA_MOVIMIENTO = 10
LINEA_META_Y = 280

class Jugador(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.volver_al_inicio()
        self.setheading(90)

    def mover_arriba(self):
        self.forward(DISTANCIA_MOVIMIENTO)

    def volver_al_inicio(self):
        self.goto(POSICION_INICIAL)

    def llego_a_la_meta(self):
        return self.ycor() > LINEA_META_Y