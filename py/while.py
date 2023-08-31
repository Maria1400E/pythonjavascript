## CICLO WHILE

i = 1

while i <= 6:
    print(f"El numero es: {i}")
    i += 1

## con la instruccion break podemos detener el ciclo
## incluso si la condicion es verdadera
print("------------------------------")
i = 1
while i <= 6:
    print(f"el numero es: {i}")
    if i == 3:
        break
    i += 1

print("------------------------------")

i = 0
while i <= 6:
    i += 1   
    if i == 3:
        continue
    print(f"el numero es: {i}")

print("------------------------------")

i = 0
while i <= 6:
    i += 1   
    if i == 3:
        continue
    print(f"el numero es: {i}")
else: 
    print("finalizooooooo")

### EJERCICIO

numPares = 0
sumaTotal = 0
numero = int(input(" Numero (-1 para terminar el programa: "))

while numero != -1:
    if numero %2==0:
        numPares+=1
        sumaTotal+=numero
    sumaNumeros = 0
    while numero!=0:
        digito = numero%10
        sumaNumeros+=digito
        numero=numero//10
    print("La suma de los digitos es: ",sumaNumeros)
    numero = int(input(" Numero (-1 para terminar el programa)"))
print(f"Se ingresaron {numPares} numeros pares")
print(f"la suma de los numeros es {sumaTotal}")
