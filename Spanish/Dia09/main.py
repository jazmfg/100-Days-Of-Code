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
    
    # Recorremos el diccionario: clave = persona, valor = oferta
    for persona, oferta in registro_ofertas.items():
        if oferta > oferta_mas_alta:
            oferta_mas_alta = oferta
            ganador = persona
            
    print(f"\nEl ganador es {ganador} con una oferta de ${oferta_mas_alta}.\n")


print("¡Bienvenido al programa de Subasta Secreta!")

# Diccionario para almacenar todas las ofertas
ofertas = {}

while True:
    
    # Guardamos el nombre en minúsculas y sin espacios innecesarios
    nombre = input("Ingresa tu nombre: ").lower().strip()

    # Evita que dos participantes usen el mismo nombre
    if nombre in ofertas:
        print("Ese nombre ya fue usado. Intenta con otro.")
        continue

    # Validamos que la oferta sea un número entero
    try:
        oferta = int(input("¿Cuál es tu oferta? $"))
    except ValueError:
        print("Ingresa un número válido.")
        continue

    # Guardamos la oferta en el diccionario
    ofertas[nombre] = oferta

    # Preguntamos si habrá más participantes
    continuar = input("¿Hay otros participantes? Escribe 'si' o 'no': ").lower().strip()
    
    if continuar != "si":
        break
    else:
        limpiar_pantalla()
        
# Una vez finalizadas todas las ofertas, buscamos al ganador
encontrar_ganador(ofertas)