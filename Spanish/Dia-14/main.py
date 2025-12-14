import os
import random
from data import datos
from arte import logo, vs

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system("cls" if os.name == "nt" else "clear")

def formatear_datos(cuenta):
    """Devuelve la información de una cuenta en un formato legible"""
    nombre = cuenta["nombre"]
    descripcion = cuenta["descripcion"]
    pais = cuenta["pais"]
    return f"{nombre}, {descripcion}, de {pais}"

def es_respuesta_correcta(seguidores_a, seguidores_b, eleccion):
    """Determina si la elección del usuario es correcta"""
    if seguidores_a > seguidores_b:
        return eleccion == "a"
    else:
        return eleccion == "b"

def juego():
    limpiar_pantalla()
    print(logo)
    
    puntuacion = 0
    seguir_jugando = True
    cuenta_b = random.choice(datos)

    while seguir_jugando:
        cuenta_a = cuenta_b
        cuenta_b = random.choice(datos)

        # Evita que A y B sean la misma cuenta
        while cuenta_a == cuenta_b:
            cuenta_b = random.choice(datos)

        print(f"A: {formatear_datos(cuenta_a)}")
        print(vs)
        print(f"B: {formatear_datos(cuenta_b)}")

        eleccion = input("¿Quién tiene más seguidores? Escribe 'A' o 'B': ").lower().strip()

        seguidores_a = cuenta_a["seguidores"]
        seguidores_b = cuenta_b["seguidores"]

        respuesta_correcta = es_respuesta_correcta(seguidores_a, seguidores_b, eleccion)

        limpiar_pantalla()
        print(logo)

        if respuesta_correcta:
            puntuacion += 1
            print(f"¡Correcto! Tu puntuación actual es: {puntuacion}\n")
        else:
            print(f"¡Incorrecto! Tu puntuación final es: {puntuacion}")
            seguir_jugando = False

juego()