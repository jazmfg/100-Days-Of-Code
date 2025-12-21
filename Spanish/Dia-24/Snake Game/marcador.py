from turtle import Turtle

ALINEACION = "center"
FUENTE = ("Courier", 24, "normal")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.puntaje = 0

        try:
            with open("data.txt") as archivo:
                self.mejor_puntaje = int(archivo.read())
        except FileNotFoundError:
            self.mejor_puntaje = 0
            with open("data.txt", mode="w") as archivo:
                archivo.write("0")

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(
            f"Puntaje: {self.puntaje}  Mejor Puntaje: {self.mejor_puntaje}",
            align=ALINEACION,
            font=FUENTE
        )

    def aumentar_puntaje(self):
        self.puntaje += 1
        self.actualizar_marcador()

    def resetear_puntaje(self):
        if self.puntaje > self.mejor_puntaje:
            self.mejor_puntaje = self.puntaje
            with open("data.txt", mode="w") as archivo:
                archivo.write(str(self.mejor_puntaje))
        self.puntaje = 0
        self.actualizar_marcador()

    def game_over(self):
        self.goto(0, 0)
        self.write("Fin del Juego", align=ALINEACION, font=FUENTE)