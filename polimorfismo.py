x = "hola"
print(len(x))
tupla = ("hola",22,31,"mundo")
print(len(tupla))

## Polimorfismo de clase 

class carro:
    def __init__(self,modelo,marca):
        self.modelo = modelo
        self.marca = marca
    
    def movimiento(self):
        print("Conducir")

class barco:
   
    def movimiento(self):
        print("Navega")

class avion(carro):
   
    def movimiento(self):
        print("Vuela")

