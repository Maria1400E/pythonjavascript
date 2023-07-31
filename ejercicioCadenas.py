## realizar un ejercio basico con el random() float y vamos a cortar el numero 1:3,inicio:6 y del fin:-4
## cadena sacar la longitud, inicio hasta longitud 
## Upper case
## Lower case

import random

numeroAleatorio = str(random.random())
corte1 = numeroAleatorio[1:3]
numeroInicio = numeroAleatorio[:6]
numeroFinal = numeroAleatorio[:-4]
print(numeroAleatorio)
print("Este es el primer corte: ",corte1)
print("Este es Inicio del segundo corte en 6: ",numeroInicio)
print("Este es el fin del segundo corte -4: ",numeroFinal)

print("-----------------------------------------")

cadena = "Esta cadena es para el ejemplo del ejercicio"
longitudCadena = len(cadena)
print("La longitud de la cadena es: ",longitudCadena)

subcadena = cadena[:longitudCadena]
print(subcadena)

