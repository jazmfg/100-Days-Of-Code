import turtle
import random

pantalla = turtle.Screen()
pantalla.setup(width=500, height=400)
pantalla.title("Carrera de Tortugas")

colores = {
    "rojo": "red",
    "naranja": "orange",
    "amarillo": "yellow",
    "verde": "green",
    "azul": "blue",
    "morado": "purple"
}

lista_colores = list(colores.keys())
tortugas = []

apuesta_usuario = pantalla.textinput(
    "Haz tu apuesta",
    f"¿Qué tortuga ganará la carrera? Elige entre: {', '.join(lista_colores)}"
)

if apuesta_usuario:
    apuesta_usuario = apuesta_usuario.lower()

posicion_inicial_y = -100
for indice, color_es in enumerate(lista_colores):
    nueva_tortuga = turtle.Turtle(shape="turtle")
    nueva_tortuga.color(colores[color_es])
    nueva_tortuga.penup()
    nueva_tortuga.goto(x=-230, y=posicion_inicial_y + indice * 40)
    tortugas.append(nueva_tortuga)

color_ganador = None
carrera_activa = True if apuesta_usuario in lista_colores else False

while carrera_activa:
    for corredora in tortugas:
        corredora.forward(random.randint(1, 10))

        if corredora.xcor() >= 230:
            color_turtle = corredora.pencolor()
            for esp, eng in colores.items():
                if eng == color_turtle:
                    color_ganador = esp
            carrera_activa = False
            break

if color_ganador == apuesta_usuario:
    print(f"Has ganado. La tortuga {color_ganador} es la ganadora.")
else:
    print(f"Has perdido. La tortuga {color_ganador} ganó la carrera.")

pantalla.exitonclick()