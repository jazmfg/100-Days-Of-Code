from turtle import Turtle

FUENTE = ("Courier", 24, "normal")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.nivel = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"Nivel: {self.nivel}", align="left", font=FUENTE)

    def aumentar_nivel(self):
        self.nivel += 1
        self.actualizar_marcador()

    def fin_del_juego(self):
        self.goto(0, 0)
        self.write("FIN DEL JUEGO", align="center", font=FUENTE)