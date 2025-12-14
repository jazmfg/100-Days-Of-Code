class CerebroCuestionario:

    def __init__(self, lista_preguntas):
        self.numero_pregunta = 0
        self.puntaje = 0
        self.lista_preguntas = lista_preguntas

    def aun_hay_preguntas(self):
        return self.numero_pregunta < len(self.lista_preguntas)

    def siguiente_pregunta(self):
        pregunta_actual = self.lista_preguntas[self.numero_pregunta]
        self.numero_pregunta += 1
        respuesta_usuario = input(
            f"P.{self.numero_pregunta}: {pregunta_actual.texto} (Verdadero/Falso): "
        )
        self.verificar_respuesta(respuesta_usuario, pregunta_actual.respuesta)

    def verificar_respuesta(self, respuesta_usuario, respuesta_correcta):
        if respuesta_usuario.lower() == respuesta_correcta.lower():
            self.puntaje += 1
            print("¡Respuesta correcta!")
        else:
            print("Respuesta incorrecta.")
        print(f"La respuesta correcta era: {respuesta_correcta}.")
        print(f"Tu puntaje actual es: {self.puntaje}/{self.numero_pregunta}")
        print("\n")