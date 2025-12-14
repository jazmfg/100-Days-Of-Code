import turtle as t
import random

# Lista de colores en formato RGB
colores = [
    (239, 246, 241), (246, 241, 239), (234, 239, 245), (220, 221, 225),
    (240, 232, 219), (228, 234, 238), (241, 209, 91), (234, 66, 31),
    (244, 229, 39), (44, 108, 140), (145, 18, 36), (27, 38, 66),
    (232, 129, 26), (37, 41, 33), (10, 97, 74), (236, 81, 108)
]

t.colormode(255)

tortuga = t.Turtle()
tortuga.penup()
tortuga.hideturtle()
tortuga.speed("fastest")

# Posición inicial de la tortuga
tortuga.setheading(225)
tortuga.forward(300)
tortuga.setheading(0)

for punto in range(1, 101):
    tortuga.dot(20, random.choice(colores))
    tortuga.forward(50)

    if punto % 10 == 0:
        tortuga.setheading(90)
        tortuga.forward(50)
        tortuga.setheading(180)
        tortuga.forward(500)
        tortuga.setheading(0)

pantalla = t.Screen()
pantalla.exitonclick()