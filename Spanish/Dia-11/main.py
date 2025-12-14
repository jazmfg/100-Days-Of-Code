import os
import random
from art import logo

def limpiar_consola():
    """Limpia la consola para comenzar un nuevo juego"""
    os.system('cls' if os.name == 'nt' else 'clear')

def repartir_carta():
    """Devuelve una carta aleatoria del mazo"""
    mazo = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(mazo)

def calcular_puntaje(mano):
    
    if sum(mano) == 21 and len(mano) == 2:
        return 0

    # Ajusta As de 11 a 1 si es necesario
    if 11 in mano and sum(mano) > 21:
        mano.remove(11)
        mano.append(1)

    return sum(mano)

def comparar_puntajes(p_jugador, p_computadora):
    """Devuelve un mensaje con el resultado del juego."""
    if p_jugador == p_computadora:
        return "Empate."
    elif p_computadora == 0:
        return "¡Perdiste! La computadora tiene Blackjack"
    elif p_jugador == 0:
        return "¡Ganaste con Blackjack!"
    elif p_jugador > 21:
        return "Te pasaste de 21. Pierdes."
    elif p_computadora > 21:
        return "La computadora se pasó de 21. ¡Ganas!"
    elif p_jugador > p_computadora:
        return "¡Ganaste!"
    else:
        return "Perdiste"

def jugar():
    """Función principal que gestiona toda la partida."""
    limpiar_consola()
    print(logo)

    mano_jugador = []
    mano_computadora = []

    # Repartir 2 cartas a cada uno
    for _ in range(2):
        mano_jugador.append(repartir_carta())
        mano_computadora.append(repartir_carta())

    juego_terminado = False

    # Turno del jugador
    while not juego_terminado:
        puntaje_jugador = calcular_puntaje(mano_jugador)
        puntaje_computadora = calcular_puntaje(mano_computadora)

        print(f"\nTus cartas: {mano_jugador}, puntuación: {puntaje_jugador}")
        print(f"Carta visible de la computadora: {mano_computadora[0]}")

        if puntaje_jugador == 0 or puntaje_computadora == 0 or puntaje_jugador > 21:
            juego_terminado = True
        else:
            eleccion = input("¿Quieres otra carta? (sí / no): ").lower()
            while eleccion not in ['si', 'no']:
                eleccion = input("Por favor escribe 'si' o 'no': ").lower()

            if eleccion == 'si':
                mano_jugador.append(repartir_carta())
            else:
                juego_terminado = True

    # Turno de la computadora
    while calcular_puntaje(mano_computadora) != 0 and calcular_puntaje(mano_computadora) < 17:
        mano_computadora.append(repartir_carta())

    # Puntajes finales
    puntaje_computadora = calcular_puntaje(mano_computadora)
    puntaje_jugador = calcular_puntaje(mano_jugador)

    print(f"\nTu mano final: {mano_jugador}, Puntuación final: {puntaje_jugador}")
    print(f"Mano final de la computadora: {mano_computadora}, Puntuación final: {puntaje_computadora}")
    print(comparar_puntajes(puntaje_jugador, puntaje_computadora))

# Bucle principal
while True:
    jugar_de_nuevo = input("\n¿Quieres jugar Blackjack? (sí / no): ").lower()
    while jugar_de_nuevo not in ['si', 'no']:
        jugar_de_nuevo = input("Por favor escribe 'si' o 'no': ").lower()
    
    if jugar_de_nuevo == 'si':
        jugar()
    else:
        print("¡Gracias por jugar!")
        break