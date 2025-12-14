import time
from turtle import Screen
from serpiente import Serpiente

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Juego de la Serpiente")
pantalla.tracer(0)

serpiente = Serpiente()

pantalla.listen()
pantalla.onkey(serpiente.arriba, "Up")
pantalla.onkey(serpiente.abajo, "Down")
pantalla.onkey(serpiente.izquierda, "Left")
pantalla.onkey(serpiente.derecha, "Right")

juego_activo = True

while juego_activo:
    pantalla.update()
    time.sleep(0.1)
    serpiente.mover()

pantalla.exitonclick()