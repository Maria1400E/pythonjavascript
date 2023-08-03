lista = [10,20,30]
totalA = 0

for precio in lista:
    totalA += precio
    print(f"total: {totalA} articulos")


## FOR ANIDADOS
## Escribir un codigo para dibujar la forma de la f

listaNum = [5,2,5,2,2]

for count in listaNum:
    salida = ""
    for count1 in range(count):
        salida += "*"

    print(salida)

## Escribir un programa que pida al usuario un numero entero y
## muestre por pantalla un triangulo rectangulo con la altuna del numero introducido

## Escriba un programa que pida al usuario un numero entero y 
## muestre por pantalla  un triangulo rectangulo con los numero y la altura del numero introducido

## Un programa que muestre por pantalla las tablas de multiplicar del 1 al 10

numero = int(input("Ingrese un numero: "))

salida = "*"

for triangulo in range(1,numero+1):
    print(salida*triangulo)

print("-------------------------------")

num = int(input("Ingrese un numero: "))

y=0
for x in range(1,num+1):
    y = (x * 2) - 1
    for z in range(y, 0, -2):
        print(z, end = ' ') 
    print()


print("-------------------------------")

multi = int(input("Ingrese el numero: "))

for m in range(1,11):
    for n in range(1):
        print(multi," x ",m," = ",multi*m)