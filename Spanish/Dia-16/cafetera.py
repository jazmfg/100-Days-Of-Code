class Cafetera:
    """Modela la máquina que prepara el café."""
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leche": 200,
            "cafe": 100,
        }

    def reporte(self):
        """Imprime un reporte de todos los recursos."""
        print(f"Agua: {self.recursos['agua']}ml")
        print(f"Leche: {self.recursos['leche']}ml")
        print(f"Café: {self.recursos['cafe']}g")

    def recursos_suficientes(self, bebida):
        """Devuelve True si el pedido se puede hacer, False si no hay suficientes ingredientes."""
        puede_hacer = True
        for ingrediente in bebida.ingredientes:
            if bebida.ingredientes[ingrediente] > self.recursos[ingrediente]:
                print(f"Lo siento, no hay suficiente {ingrediente}.")
                puede_hacer = False
        return puede_hacer

    def preparar_cafe(self, pedido):
        """Descuenta los ingredientes necesarios de los recursos."""
        for ingrediente in pedido.ingredientes:
            self.recursos[ingrediente] -= pedido.ingredientes[ingrediente]
        print(f"Aquí tienes tu {pedido.nombre}")