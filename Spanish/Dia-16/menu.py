class ElementoMenu:
    """Modela cada elemento del menú."""
    def __init__(self, nombre, agua, leche, cafe, costo):
        self.nombre = nombre
        self.costo = costo
        self.ingredientes = {
            "agua": agua,
            "leche": leche,
            "cafe": cafe
        }

class Menu:
    """Modela el menú con las bebidas."""
    def __init__(self):
        self.menu = [
            ElementoMenu(nombre="latte", agua=200, leche=150, cafe=24, costo=2.5),
            ElementoMenu(nombre="espresso", agua=50, leche=0, cafe=18, costo=1.5),
            ElementoMenu(nombre="capuccino", agua=250, leche=50, cafe=24, costo=3),
        ]

    def obtener_items(self):
        """Devuelve todos los nombres de las bebidas disponibles en el menú."""
        opciones = ""
        for item in self.menu:
            opciones += f"{item.nombre}/"
        return opciones

    def buscar_bebida(self, nombre_bebida):
        """Busca una bebida por nombre. Si existe, la retorna; si no, muestra un mensaje."""
        for item in self.menu:
            if item.nombre == nombre_bebida:
                return item
        print("Lo siento, ese artículo no está disponible.")