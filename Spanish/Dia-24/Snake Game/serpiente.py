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
        for posicion in POSICIONES_INICIALES:
            self.agregar_segmento(posicion)

    def agregar_segmento(self, posicion):
        nuevo_segmento = Turtle("square")
        nuevo_segmento.color("white")
        nuevo_segmento.penup()
        nuevo_segmento.goto(posicion)
        self.segmentos.append(nuevo_segmento)

    def crecer(self):
        self.agregar_segmento(self.segmentos[-1].position())

    def mover(self):
        for i in range(len(self.segmentos) - 1, 0, -1):
            x = self.segmentos[i - 1].xcor()
            y = self.segmentos[i - 1].ycor()
            self.segmentos[i].goto(x, y)
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

    def reiniciar(self):
        for segmento in self.segmentos:
            segmento.goto(1000, 1000)
        self.segmentos.clear()
        self.crear_serpiente()
        self.cabeza = self.segmentos[0]