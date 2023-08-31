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

class Vehiculo:
    def _init_(self):
        self.matricula = ""
        self.modelo = ""
        self.potenciacv = ""

    def imprimir(self):
        print("Matricula:", self.matricula)
        print("Modelo:", self.modelo)
        print("PotenciaCV:", self.potenciacv)


class Taxi(Vehiculo):
    def _init_(self):
        super()._init_()
        self.numerolicencia = ""

    def imprimir(self):
        print("Numero Licencia:", self.numerolicencia)


class Autobus(Vehiculo):
    def _init_(self):
        super()._init_()
        self.numeroplazas = ""

    def imprimir(self):
        print("Numero Plazas:", self.numeroplazas)


if __name__ == "_main_":
    print("\nTAXI\n")
    _Taxi1 = Taxi()
    _Taxi1.numerolicencia = input("Digite su numero de licencia: ")
    _Taxi1.matricula = input("Digite su numero de matricula: ")
    _Taxi1.modelo = input("Digite el modelo de su carro: ")
    _Taxi1.potenciacv = input("Digite la potencia de su carro: ")
    print("\n----------------------")
    _Taxi1.imprimir()

    print("\n----------------------")

    print("\nAUTOBUS\n")
    _Autobus1 = Autobus()
    _Autobus1.numeroplazas = input("Digite su numero de plazas: ")
    _Autobus1.matricula = input("Digite su numero de matricula: ")
    _Autobus1.modelo = input("Digite el modelo de su carro: ")
    _Autobus1.potenciacv = input("Digite la potencia de su carro: ")
    print("\n----------------------")
    _Autobus1.imprimir()