from turtle import Turtle
import random

COLORES = ["red", "pink", "yellow", "green", "blue", "purple"]
VELOCIDAD_INICIAL = 5
INCREMENTO_VELOCIDAD = 10

class GestorAutos:

    def __init__(self):
        self.todos_los_autos = []
        self.velocidad_autos = VELOCIDAD_INICIAL

    def crear_auto(self):
        probabilidad = random.randint(1, 6)
        if probabilidad == 1:
            nuevo_auto = Turtle("square")
            nuevo_auto.shapesize(stretch_wid=1, stretch_len=2)
            nuevo_auto.penup()
            nuevo_auto.color(random.choice(COLORES))
            posicion_y = random.randint(-250, 250)
            nuevo_auto.goto(300, posicion_y)
            self.todos_los_autos.append(nuevo_auto)

    def mover_autos(self):
        for auto in self.todos_los_autos:
            auto.backward(self.velocidad_autos)

    def subir_nivel(self):
        self.velocidad_autos += INCREMENTO_VELOCIDAD