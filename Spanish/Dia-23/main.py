import time
from turtle import Screen
from jugador import Jugador
from marcador import Marcador
from gestor_autos import GestorAutos

pantalla = Screen()
pantalla.setup(width=600, height=600)
pantalla.tracer(0)

jugador = Jugador()
gestor_autos = GestorAutos()
marcador = Marcador()

pantalla.listen()
pantalla.onkey(jugador.mover_arriba, "Up")

juego_activo = True
while juego_activo:
    time.sleep(0.1)
    pantalla.update()

    gestor_autos.crear_auto()
    gestor_autos.mover_autos()

    for auto in gestor_autos.todos_los_autos:
        if auto.distance(jugador) < 20:
            juego_activo = False
            marcador.fin_del_juego()

    if jugador.llego_a_la_meta():
        jugador.volver_al_inicio()
        gestor_autos.subir_nivel()
        marcador.aumentar_nivel()

pantalla.exitonclick()