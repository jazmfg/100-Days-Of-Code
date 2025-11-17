import random

print("\n*** piedra, papel o tijera ***\n")

piedra = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

papel = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

tijera = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

dibujo = {
    "piedra": piedra,
    "papel": papel,
    "tijera": tijera
}

opciones = ["piedra", "papel", "tijera"]

usuario = input("Elige una opción (piedra, papel o tijera): ").strip().lower()

if usuario not in opciones:
    print("Por favor elige piedra, papel o tijera")
else:
    computadora = random.choice(opciones)
    
    print(f"\nComputadora eligió: {computadora}")
    print(dibujo[computadora])

    print(f"\nTú elegiste: {usuario}")
    print(dibujo[usuario])

    if computadora == usuario:
        print("¡Empate!")
        
    elif (computadora == "piedra" and usuario == "tijera") or (computadora == "papel" and usuario == "piedra") or (computadora == "tijera" and usuario == "papel"): 
        print("Computadora gana")
    
    else:
        print("Tú ganas")