from datosCliente import Cliente

class Pedido(Cliente):
    def __init__(self, nombre, telefono, totalP, totalM, totalG, tamaño):
        super().__init__(nombre, telefono)
        self.totalP = totalP
        self.totalM = totalM
        self.totalG = totalG
        self.tamaño = tamaño
    
    def totalPedido(self):
        if self.tamaño == "1/2 litro":
            print("El helado tiene un precio de:", self.totalP)
            print()
        elif self.tamaño == "1 litro":
            print("El helado tiene un precio de:", self.totalM)
            print()
        else:
            print("El helado tiene un precio de:", self.totalG)
            print()


