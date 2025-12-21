import time
from turtle import Screen
from paleta import Paleta
from pelota import Pelota
from marcador import Marcador

pantalla = Screen()
pantalla.bgcolor("black")
pantalla.setup(width=800, height=600)
pantalla.title("Ping Pong")
pantalla.tracer(0)

paleta_der = Paleta((350, 0))
paleta_izq = Paleta((-350, 0))
pelota = Pelota()
marcador = Marcador()

pantalla.listen()
pantalla.onkey(paleta_der.subir, "Up")
pantalla.onkey(paleta_der.bajar, "Down")
pantalla.onkey(paleta_izq.subir, "w")
pantalla.onkey(paleta_izq.bajar, "s")

juego_activo = True

while juego_activo:
    pantalla.update()
    time.sleep(pelota.velocidad)
    pelota.mover()

    if pelota.ycor() > 280 or pelota.ycor() < -280:
        pelota.rebotar_y()

    if (
        pelota.distance(paleta_der) < 50 and pelota.xcor() > 320
        or pelota.distance(paleta_izq) < 50 and pelota.xcor() < -320
    ):
        pelota.rebotar_x()

    if pelota.xcor() > 380:
        pelota.reiniciar()
        marcador.punto_izquierda()
        pelota.actualizar_velocidad(marcador.nivel)

    if pelota.xcor() < -380:
        pelota.reiniciar()
        marcador.punto_derecha()
        pelota.actualizar_velocidad(marcador.nivel)

    ganador = marcador.hay_ganador()
    if ganador:
        marcador.mostrar_ganador(ganador)
        juego_activo = False

pantalla.exitonclick()