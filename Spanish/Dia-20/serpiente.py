from turtle import Turtle

POSICIONES_INICIALES = [(0, 0), (-20, 0), (-40, 0)]

DISTANCIA_MOVIMIENTO = 20
ARRIBA = 90
ABAJO = 270
IZQUIERDA = 180
DERECHA = 0


class Serpiente:

    def __init__(self):
        self.segmentos = []
        self.crear_serpiente()
        self.cabeza = self.segmentos[0]

    def crear_serpiente(self):
        """Crea los segmentos iniciales de la serpiente"""
        for posicion in POSICIONES_INICIALES:
            nuevo_segmento = Turtle("square")
            nuevo_segmento.color("white")
            nuevo_segmento.penup()
            nuevo_segmento.goto(posicion)
            self.segmentos.append(nuevo_segmento)

    def mover(self):
        """Mueve la serpiente hacia adelante"""
        for indice in range(len(self.segmentos) - 1, 0, -1):
            nueva_x = self.segmentos[indice - 1].xcor()
            nueva_y = self.segmentos[indice - 1].ycor()
            self.segmentos[indice].goto(nueva_x, nueva_y)
        self.cabeza.forward(DISTANCIA_MOVIMIENTO)

    def arriba(self):
        if self.cabeza.heading() != ABAJO:
            self.cabeza.setheading(ARRIBA)

    def abajo(self):
        if self.cabeza.heading() != ARRIBA:
            self.cabeza.setheading(ABAJO)

    def izquierda(self):
        if self.cabeza.heading() != DERECHA:
            self.cabeza.setheading(IZQUIERDA)

    def derecha(self):
        if self.cabeza.heading() != IZQUIERDA:
            self.cabeza.setheading(DERECHA)