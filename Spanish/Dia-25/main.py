import turtle
import pandas

pantalla = turtle.Screen()
pantalla.title("Estados de EE.UU.")
imagen = "./imagen.gif"

pantalla.addshape(imagen)
turtle.shape(imagen)

datos = pandas.read_csv("estados.csv")
todos_los_estados = datos.state.to_list()
estados_adivinados = []

while len(estados_adivinados) < 50:
    respuesta_estado = pantalla.textinput(
        title=f"{len(estados_adivinados)}/50 Estados Correctos",
        prompt="Escribe el nombre del estado:"
    ).title()

    if respuesta_estado == "Salir":
        estados_faltantes = []
        for estado in todos_los_estados:
            if estado not in estados_adivinados:
                estados_faltantes.append(estado)

        nuevos_datos = pandas.DataFrame(estados_faltantes)
        nuevos_datos.to_csv("estados_para_aprender.csv")
        break

    if respuesta_estado in todos_los_estados:
        estados_adivinados.append(respuesta_estado)

        escritor = turtle.Turtle()
        escritor.hideturtle()
        escritor.penup()

        datos_estado = datos[datos.state == respuesta_estado]
        escritor.goto(datos_estado.x.item(), datos_estado.y.item())
        escritor.write(respuesta_estado)