class persona:
    nombre = ""
    apellido = ""
    edad = 0
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    def __str__(self):
        return f"El nombre es: {self.nombre} el apellido es: {self.apellido} la edad es: {self.edad}"
persona1 = persona("Juan","Perez",23)
print(persona1)

