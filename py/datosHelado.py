from datosCliente import Cliente

class Helado(Cliente):
    def __init__(self, nombre, telefono, sabor, tamaño):
        super().__init__(nombre, telefono)
        self.sabor = sabor
        self.tamaño = tamaño
    
    def imprimir(self):
        print("Sabor: ", self.sabor)
        print("Tamaño: ", self.tamaño)