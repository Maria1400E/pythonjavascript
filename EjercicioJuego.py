import random

jugadores = {}

while True:
    nombre = input("Ingrese su nombre: ")
    numAle = random.randint(1,50)
    jugadores[nombre] = numAle ##Guarda el numero aleatorio asociado al nombre

    print("HOLA {} ,EL JUEGO HA COMENZADO".format(nombre))
    print("Intenta adivinar el numero aleatorio")
    print("Solo tienes 3 intentos")

    for intento in range(1,4):
        numero = int(input("Intento{}: Escribe un numero: ".format(intento)))

        if numero == numAle:
            print()
            print("¡FELICIDADES! {} ¡ADIVINASTE!".format(nombre))
            break
        elif numero > numAle:
            print("El numero ingresado es mayor")
        else:
            print("El numero ingresado es inferior")
    else:
        print()
        print("¡OH OH! SE TE ACABARON LOS INTENTOS")
    print()        
    print("El numero correcto era: ",numAle)
    print("EL JUEGO FINALIZÓ")
    print()
    volverJugar = input("Quiere volver a jugar? (s/n): ")
    if volverJugar.lower() != "s":
        break