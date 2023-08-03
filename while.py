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

