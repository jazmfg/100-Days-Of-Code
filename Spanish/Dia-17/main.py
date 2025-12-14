import random
from datos import datos_preguntas
from modelo import Pregunta
from cuestionario import CerebroCuestionario

banco_preguntas = []

for pregunta in datos_preguntas:
    texto_pregunta = pregunta["pregunta"]
    respuesta_correcta = pregunta["respuesta_correcta"]
    nueva_pregunta = Pregunta(texto_pregunta, respuesta_correcta)
    banco_preguntas.append(nueva_pregunta)
    
random.shuffle(banco_preguntas)
cuestionario = CerebroCuestionario(banco_preguntas)

while cuestionario.aun_hay_preguntas():
    cuestionario.siguiente_pregunta()

print("Has completado el cuestionario")
print(f"Tu puntuación final es: {cuestionario.puntaje} de {cuestionario.numero_pregunta}")