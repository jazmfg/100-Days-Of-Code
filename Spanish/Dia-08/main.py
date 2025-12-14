import string

abecedario = string.ascii_lowercase + "ñ"

def cesar(texto, desplazamiento, direccion):
    """
    - Si direccion es 'cifrar', desplaza las letras hacia adelante.
    - Si es 'descifrar', invierte el desplazamiento.
    """
    resultado = ""
    
    # Si se quiere descifrar, invertimos el desplazamiento
    if direccion == "descifrar":
        desplazamiento *= -1

    for caracter in texto:
        # Solo ciframos letras que existan en el abecedario
        if caracter in abecedario:
            posicion = abecedario.index(caracter)

            # Calculamos la nueva posición aplicando el desplazamiento
            nueva_posicion = (posicion + desplazamiento) % len(abecedario)

            # Agregamos la letra desplazada al resultado
            resultado += abecedario[nueva_posicion]
        else:
            # Si no es una letra (espacio, número, símbolo) lo dejamos igual
            resultado += caracter

    print(f"\nResultado: {resultado}\n")


# Ciclo principal del programa
ejecutar = True

while ejecutar:

    # El usuario elige si quiere cifrar o descifrar
    direccion = input("\nEscribe 'cifrar' para encriptar o 'descifrar' para desencriptar:\n").lower()
    texto = input("\nEscribe tu mensaje:\n").lower()
    desplazamiento = int(input("\nEscribe el número de desplazamiento:\n"))

    # Normalizamos el desplazamiento para que no exceda el tamaño del abecedario
    desplazamiento = desplazamiento % len(abecedario)

    # Ejecutamos la función principal del cifrado
    cesar(texto, desplazamiento, direccion)

    # Preguntamos si quiere repetir el programa
    repetir = input("¿Quieres volver a ejecutar el programa? (si/no): ").lower()
    
    if repetir == "no":
        ejecutar = False
        print("\nAdiós")