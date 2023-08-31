##Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir 
# listado, 3-finalizar programa. A continuación, el usuario debe poder 
# seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informele
#  del error. El menú se debe volver a mostrar luego de ejecutar cada opción, 
# permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
# Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
print("----------PRIMER-------------")

while True:
    print("ingrese una opcion")
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    usuario = int(input("Escriba su opcion: "))
    print()

    if usuario > 3:
        print("Acaba de escoger una opcion incorrecta")

        print("Vuelva a escoger una opción")
        print("opcion 1")
        print("opcion 2")
        print("opcion 3")
        usuario = int(input("Escriba su opcion: "))
        print()
        
    if usuario == 1:
        print("""             Python es un lenguaje de programación interpretado, versátil y de alto nivel. 
              Fue creado por Guido van Rossum y lanzadopor primera vez en 1991. Su sintaxis es 
              fácil de leer y escribir, lo que lo hace ideal tanto para principiantes como para 
              desarrolladores experimentados.""")
        print()
    
    if usuario == 2:
        print("""             JavaScript es un lenguaje de programación interpretado, dinámico y de alto nivel 
              que se utiliza principalmente para crear interactividad en páginas web. Fue desarrollado 
              por Brendan Eich en 1995 y se ha convertido en uno de los lenguajes de programación más 
              populares y ampliamente utilizados en la industria del desarrollo web.""")
        print()
        
    if usuario == 3:
        break

##Solicitar al usuario el ingreso de una frase y de una letra 
# (que puede o no estar en la frase). Recorrer la frase, carácter a carácter,
#  comparando con la letra buscada. Si el carácter no coincide, indique que 
# no hay coincidencia en esa posición (imprimiendo la posición) y continúe.
#  Si se encuentra una coincidencia, indique en qué posición se encontró y
#  finalizó la ejecución.

print()
print("----------SEGUNDOO-----------")

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
lis = []
pos = 0

while pos < len(frase):
    if frase[pos] == letra:
        lis.append(pos)
        print("La letra (",letra,") está en la frase")
        print("Está en las posiciones",lis)
    pos+=1
while letra not in frase:
    print("La letra no está en la frase")
    break
   
##Crear un programa que permita al usuario ingresar los montos de las compras 
# de un cliente (se desconoce la cantidad de datos que cargará, la cual puede 
# cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario 
# ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y 
# se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total 
# a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

print()
print("----------TERCER-----------")

totalCompra = 0
monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    
while monto != 0:
    if monto < 0:
        print("El monto ingresado es negativo. Ingrese un nuevo monto.")
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    else:
        totalCompra += monto
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))

    if totalCompra > 1000:
        descuento = totalCompra * 0.1
        totalCompra -= descuento
        print("Tiene un descuento del 10")

print("Total a pagar:", totalCompra)