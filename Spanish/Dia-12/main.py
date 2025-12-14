import random

INTENTOS_FACIL = 10
INTENTOS_DIFICIL = 5

def verificar_intento(intentado, numero_secreto, intentos_restantes):
    """
    Compara el número ingresado con el número secreto.
    Devuelve la cantidad de intentos restantes.
    """
    
    if intentado > numero_secreto:
        print("Muy alto")
        return intentos_restantes - 1
    elif intentado < numero_secreto:
        print("Muy bajo")
        return intentos_restantes - 1
    else:
        print(f"¡Correcto! El número era {numero_secreto}")
        return 0

def elegir_dificultad():
    """
    Pregunta al jugador la dificultad y retorna el número de intentos disponibles.
    """
    nivel = input("Elige dificultad 'facil' = 10 intentos / 'dificil' = 5 intentos: ").lower()
    
    if nivel == "facil":
        return INTENTOS_FACIL
    else:
        return INTENTOS_DIFICIL

def jugar():
    """Función principal del juego."""
    print("\nBienvenido a ¡Adivina el Número!\n")
    print("Estoy pensando en un número entre 1 y 100...")

    numero_secreto = random.randint(1, 100)
    intentos = elegir_dificultad()

    adivinanza = None

    while adivinanza != numero_secreto and intentos > 0:
        print(f"\nTe quedan {intentos} intentos")
        
        try:
            adivinanza = int(input("Adivina un número: "))
        except ValueError:
            print("Por favor, escribe un número válido")
            continue

        intentos = verificar_intento(adivinanza, numero_secreto, intentos)

        if adivinanza == numero_secreto:
            break
        elif intentos == 0:
            print(f"\nTe quedaste sin intentos. El número correcto era {numero_secreto}.")

jugar()