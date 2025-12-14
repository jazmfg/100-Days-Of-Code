from menu import Menu
from cafetera import Cafetera
from maquina_de_dinero import MaquinaDinero

menu = Menu()
cafetera = Cafetera()
maquina_dinero = MaquinaDinero()

maquina_encendida = True

while maquina_encendida:
    opciones = menu.obtener_items()
    eleccion = input(f"\n¿Qué te gustaría? ({opciones}): ").lower()

    if eleccion == "apagado" or eleccion == "off":
        maquina_encendida = False
        print("Apagando la máquina...")

    elif eleccion == "reporte" or eleccion == "report":
        cafetera.reporte()
        maquina_dinero.reporte()

    else:
        bebida = menu.buscar_bebida(eleccion)
        if bebida and cafetera.recursos_suficientes(bebida):
            if maquina_dinero.realizar_pago(bebida.costo):
                cafetera.preparar_cafe(bebida)