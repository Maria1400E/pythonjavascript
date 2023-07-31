# Las litas se utilizan para almacenar varios elementos en una sola variable 
## las listas son 1 de los 4 tipos incorporados en py que se utilizan para almacenar colecciones de datos 
## tuple, set, dictionary
# las listas se usan colocando []
lista=["hola", "mundo", "py"]
print(lista)
## elementos de la lista 
## los elementos de la lista estan ordenados, se pueden cambiar y permiten valores duplicados 
## los elementos de las listas estan indexados, el primer elemento con indice [0]
# ordenado 
## tiene un orden definido y no cambia 
## si se agregan nuevos elementos a la lista, los nuevos elementos se colocan al final de la lista 
## Nota: hay algunos metodos de lista que cambian el orden, pero en general el orden siempre es el mismo 
# cambiable 
# se puede eliminar, actualizar y agregar cualquier elemento 
# permite duplicados 
# dado que listas estan indexadas, las listas pueden tener elementos con el mismo valor 
## longitud listas 
# len()
print(len(lista))
## tipos de datos listas 
## los elementos pueden ser de cualquier tipo 
string=["txt","hola","hidih","uidxiud"]
interger=[78,45,23,11,10,98]
flotantes=[78.0,45.1,12,78.0,45.23,78.0]
booleanos=[True,False,False,True,True,False,True,True]
mixta=["pepito","perez",25,"veeronfrng",12552241,True]
print(string)
print(interger)
print(flotantes)
print(booleanos)
print(mixta)
## type 
print(type(mixta))
## acceso
print()
print(string[2])
print(string[1:3])
print(string[-1])
## comprobar si un articulo existe en una lista 
## para determinar si un elemento especifico existe en una lista usamos la palabra clave in
print("pepito" not in mixta)

# 5. recorrer en for interger y validar si el 98,11 existe y la cantidad
# 6. recorrer en for flotantes y validar si el 78.0 y 45.23 si no existe y la cantidad en caso de que exista 0
# 7. recorrer en for booleanos y validar  la cantidad  de true y false en caso de que exista 0
# 8. recorrer en for Mixta y validar si nombre y apellido son iguales en caso de que coincida un mensaje que indique que la persona se encontro
## luego comparar la edad y enviarle un mensaje de es mayor de edad o menor de edad segun el caso
# validar si el numero de telefono =  12552241  esta presente o no 

## hay 4 tipos de colecciones 
# 1 la lista : es una coleccion ordenada y modificable permite miembros duplicados 
# 2 tuple : es una coleccion ordenada inmutable , permite miembros duplicados 
# 3 conjunto : es una coleccion desordenada, inmutable y no indexada
# 4 diccionario: es una coleccion ordenada y modificable no hay miembros duplicados 

