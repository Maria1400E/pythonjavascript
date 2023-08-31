"""
El gobierno nacional ha decidido dar subsidio familiar 
a familias que tienen un cierto número de hijos de la siguiente manera:
 * Si no tiene hijos no recibirá subsidio
 * Si tiene un hijo, recibirá $500.000
 * Si tiene dos hijos, recibirá $1200.000
 * Si tiene tres hijos, recibirá $1800.000
 * Si tiene más de tres hijos, recibirá $3200.000
 * NOTA: Deberá validar si el usuario ingresa un número negativo,
 para esto puede hacer uso del if o cualquier otro método que 
 ud considere pertinente.

"""
while True:
    print()
    print("SUBSIDIO FAMILIAR DEL GOBIERNO NACIONAL")
    print("Para validar si es beneficiari@ debe ingresar los siguientes datos")
    nombre = input("Escriba su nombre: ")
    hijos = int(input("Escriba la cantidad de hijos  que tiene tiene: "))

    if hijos < 0:
        print("Ha ingresado un numero negativo")
        hijos = int(input("Escriba la cantidad de hijos  que tiene tiene: "))
    if hijos == 0:
        print(nombre," Usted no es beneficiari@ para el subsidio")
    if hijos == 1:
        print(nombre," Usted recibira un subsidio de $500.000")
    if hijos == 2:
        print(nombre," Usted recibira un subsidio de $1.200.000")
    if hijos == 3:
        print(nombre," Usted recibira un subsidio de $1.800.000")
    if hijos > 4:
        print(nombre," Usted recibira un subsidio de $3.200.000")
