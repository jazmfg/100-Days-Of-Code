class MaquinaDinero:

    MONEDA = "$"

    VALOR_MONEDAS = {
        "quarters": 0.25,   # 25 centavos
        "dimes": 0.10,      # 10 centavos
        "nickles": 0.05,    # 5 centavos
        "pennies": 0.01     # 1 centavo
    }

    def __init__(self):
        self.ganancia = 0
        self.dinero_recibido = 0

    def reporte(self):
        """Imprime la ganancia actual."""
        print(f"Dinero: {self.MONEDA}{self.ganancia}")

    def procesar_monedas(self):
        """Devuelve el total calculado de las monedas ingresadas."""
        print("Por favor, inserta las monedas.")
        for moneda in self.VALOR_MONEDAS:
            cantidad = int(input(f"¿Cuántas {moneda}?: "))
            self.dinero_recibido += cantidad * self.VALOR_MONEDAS[moneda]
        return self.dinero_recibido

    def realizar_pago(self, costo):
        """Retorna True si el pago es aceptado, False si es insuficiente."""
        self.procesar_monedas()
        if self.dinero_recibido >= costo:
            cambio = round(self.dinero_recibido - costo, 2)
            print(f"Aquí tienes {self.MONEDA}{cambio} de cambio.")
            self.ganancia += costo
            self.dinero_recibido = 0
            return True
        else:
            print("Lo siento, no es suficiente dinero. Dinero devuelto.")
            self.dinero_recibido = 0
            return False