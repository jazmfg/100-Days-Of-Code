def limpiar_pantalla():
    """
    Limpia la pantalla según el sistema operativo
    """
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def encontrar_ganador(registro_ofertas):
    """
    Recorre todas las ofertas y determina: quién ofertó más y cuál fue la oferta ganadora
    """
    oferta_mas_alta = 0
    ganador = ""
    
    for persona, oferta in registro_ofertas.items():
        if oferta > oferta_mas_alta:
            oferta_mas_alta = oferta
            ganador = persona
            
    print(f"\nEl ganador es {ganador} con una oferta de ${oferta_mas_alta}.\n")

print("¡Bienvenido al programa de Subasta Secreta!")

ofertas = {}

while True:
    
    nombre = input("Ingresa tu nombre: ").lower().strip()

    if nombre in ofertas:
        print("Ese nombre ya fue usado. Intenta con otro.")
        continue

    try:
        oferta = int(input("¿Cuál es tu oferta? $"))
    except ValueError:
        print("Ingresa un número válido.")
        continue

    ofertas[nombre] = oferta

    continuar = input("¿Hay otros participantes? Escribe 'si' o 'no': ").lower().strip()
    
    if continuar != "si":
        break
    else:
        limpiar_pantalla()
        
encontrar_ganador(ofertas)