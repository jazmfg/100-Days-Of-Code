MARCADOR = "[nombre]"

with open("./Entrada/Nombres/nombres.txt") as archivo_nombres:
    nombres = archivo_nombres.readlines()

with open("./Entrada/Cartas/invitacion.txt") as archivo_carta:
    contenido_carta = archivo_carta.read()

    for nombre in nombres:
        nombre_limpio = nombre.strip()
        carta_personalizada = contenido_carta.replace(MARCADOR, nombre_limpio)

        with open(f"./Salida/carta_para_{nombre_limpio}.txt", mode="w") as carta_final:
            carta_final.write(carta_personalizada)