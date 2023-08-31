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



