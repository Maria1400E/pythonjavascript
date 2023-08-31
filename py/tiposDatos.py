"""
Conversion

en py se puede identificar el tipo de dato de una variable por medio
de la conversion

"""
## int

numero = int(3.45)
print(numero)
print(type(numero))
numero = str(3)
print(numero)
print(type(numero))
numero = int(45)
print(numero)
print(type(numero))

##float
decimal = float(12)
print(decimal)
print(type(decimal))
decimal = float("45.3")
print(decimal)
print(type(decimal))
decimal = float(78.2)
print(decimal)
print(type(decimal))

"""
TIPOS DE DATOS INCORPORADOS

* Tipo de texto str
* Tipo numerico int, float, complex ( Es un dato imaginario y se escriben con una "j")
* Tipo secuencia list, tuplas, range
* Tipo mapeo dict
* Boolean bool
* Tipo binario byt, bytearray, memoryview
* Ningun tipo nonetype

"""

"""
NUMEROS ALEATORIOS

py no tiene una funcion random() para trabajar con numeros aleatorios
pero tiene un modulo integrado llamado random que se puede usar para realizar
numeros aleatorios 

"""
import random
print(random.randrange(1,101))

"""
PY TIENE UN CONJUNTO DE METODOS
randint()
"""
print(random.randint(1,100))

## getStates()

print(random.getstate())

## random()
print(random.random())
