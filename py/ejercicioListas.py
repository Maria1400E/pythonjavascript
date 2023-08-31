# 1. recorrer en for interger y validar si el 98,11 existe y la cantidad
# 2. recorrer en for flotantes y validar si el 78.0 y 45.23 si no existe y la cantidad en caso de que exista 0
# 3. recorrer en for booleanos y validar  la cantidad  de true y false en caso de que exista 0
# 4. recorrer en for Mixta y validar si nombre y apellido son iguales en caso de que coincida un mensaje que indique que la persona se encontro
## luego comparar la edad y enviarle un mensaje de es mayor de edad o menor de edad segun el caso
## 5. validar si el numero de telefono =  12552241  esta presente o no 

string=["txt","hola","hidih","uidxiud"]
interger=[78,45,23,11,10,98]
flotantes=[78.0,45.1,12,78.0,45.23,78.0]
booleanos=[True,False,False,True,True,False,True,True]
mixta=["pepito","perez",25,"veeronfrng",12552241,True]


x=0
for element in interger:
    if element == 11:
        x=x+1
print("11 está presente en el texto", x ,"veces")

x=0
for element in interger:
    if element == 98:
        x=x+1
print("98 está presente en el texto", x ,"veces")

print("-----------------------------------------")

p1=flotantes.count(78.0)
for elemento in flotantes:
    if 78.0 == 0:
        print("El numero 78.0 no existe")
        break
    else:
        print("Hay", p1 ,"(78.0)")
        break


p2=flotantes.count(45.23)
for elemento in flotantes:
    if 45.23 == 0:
        print("El numero 45.23 no existe")
        break
    else:
        print("Hay", p2 ,"(45.23)")
        break


print("-----------------------------------------")

x=0
for elem in booleanos:
    if elem == True:
        x=x+1
print("True está presente en el texto", x ,"veces")

x=0
for elem in booleanos:
    if elem == False:
        x=x+1
print("False está presente en el texto", x ,"veces")

print("-----------------------------------------")

edad = mixta[2]
for x in mixta:
    if ("pepito" in mixta and "perez" in mixta and edad >= 18 and 12552241 in mixta):
        print("La persona se encontró")
        print("La persona es mayor de edad")
        print("El numero está correcto")
        break
    else:
        print("La persona no se encontró")
        break