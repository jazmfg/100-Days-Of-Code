import random
from arte import etapas, logo
from palabras import lista_palabras

print(logo)

#  Elegir palabra aleatoria
palabra = random.choice(lista_palabras)
longitud_palabra = len(palabra)

# Crear "pantalla" con guiones bajos
pantalla = ["_"] * longitud_palabra

# Cantidad de vidas
vidas = len(etapas) - 1

# Variable para controlar el juego
juego_terminado = False

# Bucle principal
while not juego_terminado:
    letra_usuario = input("\nAdivina una letra: ").lower()

    # Verificar si ya la había adivinado
    if letra_usuario in pantalla:
        print(f"Ya habías adivinado la letra '{letra_usuario}'.")

    # Revisar si la letra está en la palabra
    for posicion in range(longitud_palabra):
        if palabra[posicion] == letra_usuario:
            pantalla[posicion] = letra_usuario

    # Mostrar la pantalla actualizada
    print(" ".join(pantalla))

    # Si la letra no está en la palabra
    if letra_usuario not in palabra:
        vidas -= 1
        print(f"\nLa letra '{letra_usuario}' no está en la palabra. Te quedan {vidas} vidas.")
        
        if vidas == 0:
            juego_terminado = True
            print("¡Perdiste!")
            print(f"La palabra era: {palabra}.")

    # Revisar si ganó
    if "_" not in pantalla:
        juego_terminado = True
        print("¡Felicidades, ganaste!")

    # Mostrar dibujo actual del ahorcado
    print(etapas[vidas])