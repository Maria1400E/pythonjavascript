"""
DICCIONARIOS

En Python, los diccionarios son una estructura de datos que nos permite almacenar 
datos en pares clave-valor. Cada elemento del diccionario tiene una clave única que 
se utiliza para acceder a su valor asociado. Los diccionarios son muy útiles cuando 
necesitas almacenar y recuperar datos rápidamente utilizando una clave en lugar de un 
índice numérico.

"""


# Crear un diccionario vacío
miDiccionario = {}

# Agregar elementos al diccionario
miDiccionario["nombre"] = "Juan"
miDiccionario["edad"] = 30
miDiccionario["ocupacion"] = "Ingeniero"
print("El es  ",miDiccionario["nombre"]," tiene ",miDiccionario["edad"]," años y el es un ",miDiccionario["ocupacion"])