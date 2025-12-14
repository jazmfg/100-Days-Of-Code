import os      
from arte import logo

def limpiar():
    """Limpia la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    return n1 / n2

operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

def calculadora():
    
    print(logo)

    num1 = float(input("Ingresa el primer número: "))

    continuar = True  
    
    while continuar:
        print("\nOperaciones disponibles:\n")
        
        for simbolo in operaciones:
            print(simbolo, "\n")

        simbolo = input("Elige una operación: ").strip()

        if simbolo not in operaciones:
            print("Operación inválida. Intenta de nuevo.")
            continue

        num2 = float(input("Ingresa el siguiente número: "))

        if simbolo == "/" and num2 == 0:
            print("Error: no puedes dividir entre cero.")
            continue

        funcion = operaciones[simbolo]

        resultado = funcion(num1, num2)

        print(f"\n{num1} {simbolo} {num2} = {resultado:.2f}")

        eleccion = input("\nEscribe 'si' para continuar con el resultado o 'no' para comenzar una nueva operación: ").lower().strip()

        if eleccion == "si":
            num1 = resultado
        else:
            continuar = False
            limpiar()
            calculadora()

calculadora()