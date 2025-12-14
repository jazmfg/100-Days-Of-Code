MENU = {
    "espresso": {
        "ingredientes": {
            "agua": 50,
            "cafe": 18,
        },
        "costo": 1.5,
    },
    "latte": {
        "ingredientes": {
            "agua": 200,
            "leche": 150,
            "cafe": 24,
        },
        "costo": 2.5,
    },
    "capuccino": {
        "ingredientes": {
            "agua": 250,
            "leche": 100,
            "cafe": 24,
        },
        "costo": 3.0,
    }
}

recursos = {
    "agua": 300,
    "leche": 200,
    "cafe": 100,
}

dinero = 0.0

def reporte():
    """Imprime el reporte actual de recursos y dinero"""
    print(f"Agua: {recursos['agua']}ml")
    print(f"Leche: {recursos['leche']}ml")
    print(f"Café: {recursos['cafe']}g")
    print(f"Dinero: ${dinero:.2f}")

def revisar_recursos(ingredientes_pedido):
    """Revisa si hay suficientes ingredientes para preparar la bebida"""
    for item in ingredientes_pedido:
        if recursos[item] < ingredientes_pedido[item]:
            print(f"Lo siento, no hay suficiente {item}")
            return False
    return True

def procesar_monedas():
    """Calcula el total introducido por el usuario usando monedas de EE.UU."""
    print("Por favor, inserta las monedas.")

    # Diccionario con el valor de cada tipo de moneda
    monedas = {
        "quarters": 0.25,  # 25 centavos
        "dimes": 0.10,     # 10 centavos
        "nickels": 0.05,   # 5 centavos
        "pennies": 0.01    # 1 centavo
    }

    total = 0.0

    # Recorremos el diccionario para pedir la cantidad de cada moneda
    for nombre, valor in monedas.items():
        cantidad = int(input(f"¿Cuántos {nombre}? ({valor} dólares cada uno): "))
        total += cantidad * valor

    return total

def preparar_cafe(nombre_bebida, ingredientes):
    """Resta los ingredientes utilizados y sirve la bebida."""
    for item in ingredientes:
        recursos[item] -= ingredientes[item]
    print(f"Aquí tienes tu {nombre_bebida}.")

encendido = True

while encendido:
    eleccion = input("¿Qué te gustaría? (espresso/latte/capuchino): ").lower()

    if eleccion == "off":
        encendido = False

    elif eleccion == "reporte":
        reporte()

    elif eleccion in MENU:
        bebida = MENU[eleccion]
        if revisar_recursos(bebida["ingredientes"]):
            pago = procesar_monedas()
            if pago >= bebida["costo"]:
                cambio = round(pago - bebida["costo"], 2)
                if cambio > 0:
                    print(f"Aquí tienes ${cambio:.2f} de cambio.")
                dinero += bebida["costo"]
                preparar_cafe(eleccion, bebida["ingredientes"])
            else:
                print("Lo siento, no es suficiente dinero. Dinero devuelto.")
    else:
        print("Opción inválida. Por favor elige espresso, latte o capuchino.")