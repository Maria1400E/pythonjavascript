print("BIENVENIDO A LA HELADERIA FRUTIFANTASTIK")
print("Si quieres realizar un pedido debes llenar la siguiente información")
print()

class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    
    def realizarPedido(self):
        print("Nombre: ", self.nombre)
        print("Telefono: ", self.telefono)

class Helado(Cliente):
    def __init__(self, nombre, telefono, sabor, tamaño):
        super().__init__(nombre, telefono)
        self.sabor = sabor
        self.tamaño = tamaño
    
    def imprimir(self):
        print("Sabor: ", self.sabor)
        print("Tamaño: ", self.tamaño)

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
        elif self.tamaño == "1 litro":
            print("El helado tiene un precio de:", self.totalM)
        else:
            print("El helado tiene un precio de:", self.totalG)

if __name__ == "__main__":
    print("--------- PEDIDO FRUTIFANTASTIK -----------")
    nombre_cliente = input("Ingrese su nombre: ")
    telefono_cliente = input("Ingrese su numero de telefono: ")
    cliente1 = Cliente(nombre_cliente, telefono_cliente)

    sabor_helado = input("De qué sabor quieres tu helado?: ")
    tamaño_helado = input("Escoge un tamaño (1/2 litro, 1 litro, 2 litros): ")
    helado1 = Helado(nombre_cliente, telefono_cliente, sabor_helado, tamaño_helado)

    print("---------- FACTURA FRUTIFANTASTIK ------------------")
    cliente1.realizarPedido()
    helado1.imprimir()
    
    print("------------- TOTAL ----------------")
    total_pedido1 = Pedido(nombre_cliente, telefono_cliente, 5000, 20000, 40000, tamaño_helado)
    total_pedido1.totalPedido()
## Hola
