from turtle import Turtle

PUNTAJE_MAXIMO = 3
ALINEACION = "center"
FUENTE = ("Courier", 40, "bold")

class Marcador(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.puntaje_izq = 0
        self.puntaje_der = 0
        self.nivel = 1
        self.actualizar()

    def actualizar(self):
        self.clear()
        self.goto(-200, 230)
        self.write(self.puntaje_izq, align=ALINEACION, font=FUENTE)
        self.goto(200, 230)
        self.write(self.puntaje_der, align=ALINEACION, font=FUENTE)

        self.goto(0, 260)
        self.write(f"Nivel {self.nivel}", align=ALINEACION, font=("Courier", 20, "normal"))

    def actualizar_nivel(self):
        puntos_totales = self.puntaje_izq + self.puntaje_der

        if puntos_totales >= 3:
            self.nivel = 3
        elif puntos_totales >= 2:
            self.nivel = 2
        else:
            self.nivel = 1

    def punto_izquierda(self):
        self.puntaje_izq += 1
        self.actualizar_nivel()
        self.actualizar()

    def punto_derecha(self):
        self.puntaje_der += 1
        self.actualizar_nivel()
        self.actualizar()

    def hay_ganador(self):
        if self.puntaje_izq >= PUNTAJE_MAXIMO:
            return "IZQUIERDA"
        if self.puntaje_der >= PUNTAJE_MAXIMO:
            return "DERECHA"
        return None

    def mostrar_ganador(self, ganador):
        self.goto(0, 0)
        self.write(
            f"GANA JUGADOR {ganador}",
            align=ALINEACION,
            font=("Courier", 30, "bold")
        )