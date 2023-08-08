import random
numAle = random.randint(1,50)


print("EL JUEGO HA COMENZADO")
print("Intenta adivinar el numero aleatorio")
print("Solo tienes 3 intentos")

for intento in range(1,4):
    numero = int(input("Intento{}: Escribe un numero: ".format(intento)))

    if numero == numAle:
        print()
        print("¡FELICIDADES!¡ADIVINASTE!")
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