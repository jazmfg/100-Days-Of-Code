print("\n*** Isla del tesoro ***\n")

eleccion1 = input("Te encuentras en una encrucijada, ¿hacia dónde deseas ir? 'izquierda' o 'derecha':\n").strip().lower()

if eleccion1 == "izquierda":
    print("\nHas llegado a un lago grande y profundo\n")
    
    eleccion2 = input("Si deseas esperar un barco escribe 'esperar' o si deseas cruzar nadando escribe 'nadar':\n").strip().lower()
    
    if eleccion2 == "esperar":
        print("\nHas llegado a una isla\n")
        
        eleccion3 = input("Has encontrado una casa con 3 puertas: 'roja', 'amarilla' y 'azul'. Elige una:\n").strip().lower()
        
        if eleccion3 == "roja":
            print("\nHas entrado a una habitación llena de fuego ¡Fin del juego!\n")
            
        elif eleccion3 == "amarilla":
            print("\nHas encontrado el tesoro ¡Felicidades, has ganado!\n")
            
        elif eleccion3 == "azul":
            print("\nHas entrado en una habitación llena de cocodrilos ¡Fin del juego!\n")
        
        else: 
            print("\nSolo puedes escoger una de las siguientes opciones: 'roja', 'amarilla', 'azul'\n")
        
    elif eleccion2 == "nadar":
        print("\nTe ha mordido una trucha ¡Fin del juego!\n")
        
    else:
        print("\nSolo puedes escribir 'nadar' o 'esperar'\n")
    
elif eleccion1 == "derecha":
    print("\nHas caído en un agujero ¡Fin del juego!\n")
    
else:
    print("\nSolo puedes elegir 'izquierda' o 'derecha'\n")