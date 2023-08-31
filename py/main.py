from datosCliente import Cliente
from datosHelado import Helado
from datosPedido import Pedido

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
