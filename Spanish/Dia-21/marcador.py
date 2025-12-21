from turtle import Turtle

ALINEACION = "center"
FUENTE = ("Courier", 24, "normal")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.puntaje = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.actualizar_marcador()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"Puntaje: {self.puntaje}", align=ALINEACION, font=FUENTE)

    def aumentar_puntaje(self):
        self.puntaje += 1
        self.actualizar_marcador()

    def fin_del_juego(self):
        self.goto(0, 0)
        self.write("FIN DEL JUEGO", align=ALINEACION, font=FUENTE)