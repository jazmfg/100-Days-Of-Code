import time
from turtle import Screen
from comida import Comida
from marcador import Marcador
from serpiente import Serpiente


pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.bgcolor("black")
pantalla.title("Juego de la Serpiente")
pantalla.tracer(0)

serpiente = Serpiente()
comida = Comida()
marcador = Marcador()

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

    if serpiente.cabeza.distance(comida) < 15:
        comida.refrescar()
        serpiente.crecer()
        marcador.aumentar_puntaje()

    if (
        serpiente.cabeza.xcor() > 280
        or serpiente.cabeza.xcor() < -280
        or serpiente.cabeza.ycor() > 280
        or serpiente.cabeza.ycor() < -280
    ):
        juego_activo = False
        marcador.fin_del_juego()

    for segmento in serpiente.segmentos[1:]:
        if serpiente.cabeza.distance(segmento) < 10:
            juego_activo = False
            marcador.fin_del_juego()

pantalla.exitonclick()