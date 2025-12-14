import string

abecedario = string.ascii_lowercase + "ñ"

def cesar(texto, desplazamiento, direccion):
    """
    - Si direccion es 'cifrar', desplaza las letras hacia adelante.
    - Si es 'descifrar', invierte el desplazamiento.
    """
    resultado = ""
    
    if direccion == "descifrar":
        desplazamiento *= -1

    for caracter in texto:
        if caracter in abecedario:
            posicion = abecedario.index(caracter)
            nueva_posicion = (posicion + desplazamiento) % len(abecedario)
            resultado += abecedario[nueva_posicion]
        else:
            resultado += caracter

    print(f"\nResultado: {resultado}\n")

ejecutar = True

while ejecutar:

    direccion = input("\nEscribe 'cifrar' para encriptar o 'descifrar' para desencriptar:\n").lower()
    texto = input("\nEscribe tu mensaje:\n").lower()
    desplazamiento = int(input("\nEscribe el número de desplazamiento:\n"))

    desplazamiento = desplazamiento % len(abecedario)
    cesar(texto, desplazamiento, direccion)

    repetir = input("¿Quieres volver a ejecutar el programa? (si/no): ").lower()
    
    if repetir == "no":
        ejecutar = False
        print("\nAdiós")