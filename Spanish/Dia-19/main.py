import turtle
import random

pantalla = turtle.Screen()
pantalla.setup(width=500, height=400)
pantalla.title("Carrera de Tortugas")

colores = {
    "rojo": "red",
    "naranja": "orange",
    "rosa": "pink",
    "verde": "green",
    "azul": "blue",
    "morado": "purple"
}

lista_colores = list(colores.keys())
tortugas = []

apuesta_usuario = pantalla.textinput(
    "Haz tu apuesta",
    f"Elige una tortuga entre: {', '.join(lista_colores)}"
)

if apuesta_usuario:
    apuesta_usuario = apuesta_usuario.lower().strip()

posicion_inicial_y = -100
for indice, color_es in enumerate(lista_colores):
    tortuga = turtle.Turtle(shape="turtle")
    tortuga.color(colores[color_es])
    tortuga.penup()
    tortuga.goto(x=-230, y=posicion_inicial_y + indice * 40)

    tortuga.color_esp = color_es
    tortugas.append(tortuga)

carrera_activa = apuesta_usuario in lista_colores
color_ganador = None

while carrera_activa:
    for tortuga in tortugas:
        tortuga.forward(random.randint(1, 10))

        if tortuga.xcor() >= 230:
            color_ganador = tortuga.color_esp
            carrera_activa = False
            break

if color_ganador:
    if color_ganador == apuesta_usuario:
        print(f"¡Has ganado! La tortuga {color_ganador} ganó la carrera.")
    else:
        print(f"¡Has perdido! La tortuga {color_ganador} ganó la carrera.")

pantalla.exitonclick()