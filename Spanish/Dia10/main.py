from art import logo
import os      

def limpiar():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Funciones matemáticas básicas
def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

# Diccionario que relaciona símbolos con funciones
operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

def calculadora():
    
    print(logo)

    # Primer número ingresado por el usuario
    num1 = float(input("Ingresa el primer número: "))

    continuar = True  
    
    while continuar:
        # Muestra los símbolos de operaciones disponibles
        print("\nOperaciones disponibles:\n")
        for simbolo in operaciones:
            print(simbolo, "\n")

        simbolo = input("Elige una operación: ")

        # Valida si el símbolo no existe en el diccionario
        if simbolo not in operaciones:
            print("Operación inválida. Intenta de nuevo.")
            continue

        num2 = float(input("Ingresa el siguiente número: "))

        # Validación de división entre cero
        if simbolo == "/" and num2 == 0:
            print("Error: no puedes dividir entre cero.")
            continue

        funcion = operaciones[simbolo]

        # Ejecuta la operación
        resultado = funcion(num1, num2)

        # Muestra el resultado
        print(f"\n{num1} {simbolo} {num2} = {resultado}")

        # Pregunta si se continúa operando con el resultado
        eleccion = input("\nEscribe 'si' para continuar con el resultado o 'no' para comenzar una nueva operación: ").lower()

        if eleccion == "si":
            # El resultado pasa a ser el nuevo primer número
            num1 = resultado
        else:
            # Reinicia la calculadora completa
            continuar = False
            limpiar()
            calculadora()

# Inicia el programa
calculadora()