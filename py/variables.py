## Las variables son contenedores para almacenar valores de datos
## Creación de variable
## Python no tiene ningun comando o tipo de dato para declarar una variable
## Una variable se crea en el momento en que se le asigna un valor

carro="Hola"
caracter='A'

## "", '' Cadenas de texto
## Las cadenas ""
## Los caracteres ''

##Obtener el tipo
## Podemos obtener el tipo de dato de una variable con el type()
print(type(carro))
print(type(caracter))

entero=45
Entero=78
decimal=45.25
boolean=45<5
boolean1=True
boolean2=False

print(type(entero))
print(type(decimal))
print(type(boolean))
print(type(boolean1))
print(type(boolean2))

## Distingue entre mayusculas y minusculas
print(entero)
print(Entero)

## Camel Case = registroEmpleados tambien se usa en nombres de variables y funciones.

## Pascal Case = nombramientos de clases y nombres de archivos
## class Vehiculos > la primera letra en mayuscula
## class RegistroVehiculos > todas las primeras letras de las palabras en mayuscula 

## Serpiente = registro_Empleado

"""
NOMBRES DE VARIABLES

Un nombre siempre comienza con una letra _

_manzana=12 > solamente si estoy trabajndo con serpiente
manzana=89

"""

contador,valor,registroUsuario = 0, 100, "pedro"
print(contador)
print(valor)
print(registroUsuario)

contador=valor=registroUsuario="Hola"
print(contador)
print(valor)
print(registroUsuario)
print(contador,valor,registroUsuario)



