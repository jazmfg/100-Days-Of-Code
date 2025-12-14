import string
import random

numeros = string.digits
letras = string.ascii_letters
simbolos = string.punctuation

eleccion_letras = int(input("Cuántas letras quieres en tu contraseña: "))
eleccion_numeros =  int(input("Cuántos números quieres en tu contraseña: "))
eleccion_simbolos = int(input("Cuántos simbolos quieres en tu contraseña: "))

contraseña = []

for _ in range(eleccion_letras):
    contraseña.append(random.choice(letras))

for _ in range(eleccion_numeros):
    contraseña.append(random.choice(numeros))

for _ in range(eleccion_simbolos): 
    contraseña.append(random.choice(simbolos))
    
random.shuffle(contraseña)

contraseña_final = "".join(contraseña)
print(f"Tu contraseña es: {contraseña_final}")