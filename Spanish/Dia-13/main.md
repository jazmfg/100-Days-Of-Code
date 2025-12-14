## 1. Describe el Problema

Primero explica qué debería hacer el código vs qué está haciendo realmente

```python
# Incorrecto:

def mi_funcion():
    for i in range(1, 20):
        if i == 20:
           print("¡Lo lograste!")

mi_funcion()
```

```python
# Correcto:

def mi_funcion():
    for i in range(1, 21):
        if i == 20:
            print("¡Lo lograste!")

mi_funcion()
```

## 2. Reproduce el Error

Asegúrate de que el error ocurra de manera consistente para poder estudiarlo

```python
# Incorrecto:

imagen_dados = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
numero_dados = randint(1, 6)
print(imagen_dados[numero_dados])
```

```python
# Correcto:

imagen_dados = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]
numero_dados = randint(0, 5)
print(imagen_dados[numero_dados])
```
## 3. Juega a ser la Computadora

Lee el código línea por línea como si fueras la máquina

```python
# Incorrecto:

año = int(input("¿En qué año naciste? "))

if año > 1980 and año < 1994:
    print("Eres millennial")
elif año > 1994:
    print("Eres Gen Z")
```

```python
# Correcto:

año = int(input("¿En qué año naciste? "))

if 1980 < año < 1994:
    print("Eres millennial")
elif año >= 1994:
    print("Eres Gen Z")
```

## 4. Corrige los errores

Atención a comillas, indentación, comparaciones y tipos de datos

```python
# Incorrecto:

edad = input("¿Cuántos años tienes? ")
if edad > 18:
    print("Puedes conducir a los {edad}.")
```

```python
# Correcto:

try:
    edad = int(input("¿Cuántos años tienes? "))
except ValueError:
    print("Entrada inválida. Debes escribir un número.")
else:
    if edad > 18:
        print(f"Puedes conducir a los {edad}.")
```

## 5. Aplasta Bugs con print()

Usa print() para revisar valores internos y detectar comportamientos inesperados

```python
# Incorrecto:

palabra_por_pagina = 0
paginas = int(input("Número de páginas: "))
palabra_por_pagina == int(input("Palabras por página: "))

total_palabras = paginas * palabra_por_pagina
print(total_palabras)
```

```python
# Correcto:

palabra_por_pagina = int(input("Palabras por página: "))
paginas = int(input("Número de páginas: "))

total_palabras = paginas * palabra_por_pagina
print(total_palabras)
```

## 6. Usa un Depurador

A veces print() no es suficiente.
Puedes usar un depurador para ver paso a paso qué está pasando.

```python
import random
import maths

# Incorrecto:

def mutar(lista):
    lista_b = []
    nuevo_item = 0

    for item in lista:
        nuevo_item = item * 2
        nuevo_item += random.randint(1, 3)
        nuevo_item = maths.add(nuevo_item, item)

    lista_b.append(nuevo_item)
    print(lista_b)

mutar([1, 2, 3, 5, 8, 13])
```

```python
# Correcto:

def mutar(lista):
    lista_b = []

    for item in lista:
        nuevo_item = item * 2
        nuevo_item += random.randint(1, 3)
        nuevo_item = maths.add(nuevo_item, item)
        lista_b.append(nuevo_item)

    print(lista_b)

mutar([1, 2, 3, 5, 8, 13])
```