import random
from arte import etapas, logo
from palabras import lista_palabras

print(logo)

palabra = random.choice(lista_palabras)
longitud_palabra = len(palabra)

pantalla = ["_"] * longitud_palabra

vidas = len(etapas) - 1

juego_terminado = False

while not juego_terminado:
    letra_usuario = input("\nAdivina una letra: ").lower()

    if letra_usuario in pantalla:
        print(f"Ya habías adivinado la letra '{letra_usuario}'.")

    for posicion in range(longitud_palabra):
        if palabra[posicion] == letra_usuario:
            pantalla[posicion] = letra_usuario

    print(" ".join(pantalla))

    if letra_usuario not in palabra:
        vidas -= 1
        print(f"\nLa letra '{letra_usuario}' no está en la palabra. Te quedan {vidas} vidas.")
        
        if vidas == 0:
            juego_terminado = True
            print("¡Perdiste!")
            print(f"La palabra era: {palabra}.")

    if "_" not in pantalla:
        juego_terminado = True
        print("¡Felicidades, ganaste!")

    print(etapas[vidas])