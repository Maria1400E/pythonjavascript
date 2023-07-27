"""
CADENAS PY

las cadenas de trabjan con " o '
la función print pra mostrar texto ""

CADENA MULTILINEA
Podemos asignar una cadena a una variable usando 3 comillas dobles

"""

txt="""
 es simplemente el texto de relleno de las imprentas y 
 archivos de texto. Lorem Ipsum ha sido el texto de relleno 
 estándar de las industrias desde el año 1500, cuando un impresor 
 (N. del T. persona que se dedica a la imprenta) desconocido usó una 
 galería de textos y los mezcló de tal manera que logró hacer un libro
 de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó
 como texto de relleno en documentos electrónicos, quedando esencialmente 
 igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset",
 las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de .
 autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem 
 Ipsum.
"""
print(txt)
txt1="Lorem Ipsum es simplemente el texto de relleno de las"
#Nota: en el resultado, los saltos de linea se insertan en la misma posicion que en el codigo

## LAS CADENAS SON MATRICES
## Se puede acceder a los elementos de la cadena por []

print(txt[1])

## CADENA ATRAVES DE UN CICLO

for elemento in txt:
    print(elemento)

# len() para obtener la longitud de una cadena 

print(len(txt))

## COMPROBAR CADENAS

print("hola" in txt)

## not in

print("hola" not in txt)

### ejercio
## 1. valide si las palabras simplemente,estándar,estandar,(.)," ",(,) # existen
## 2. valide si las palabras juan,archivos,estan,hola,tex," ",(,) # No existen
# 3. recorrer en for txt y validar si el caracter i existe y la cantidad
# 4. recorrer en for txt y validar si el caracter " " existe y la cantidad
# 5. recorrer en for txt y validar si el caracter , existe y la cantidad
# 6. recorrer en for txt y validar si el caracter Lorem no existe y la cantidad en caso de que exista 0
# 7. recorrer en for txt y validar si el caracter hola no existe y la cantidad en caso de que exista 0

# 1.

print("PRIMER PUNTO")

print("simplemente" in txt)
print("estándar" in txt)
print("estandar" in txt)
print("." in txt)
print(" " in txt)
print("," in txt)

#2.

print("SEGUNDO PUNTO")

print("juan" not in txt)
print("archivos" not in txt)
print("estan" not in txt)
print("hola" not in txt)
print("tex" not in txt)
print(" " not in txt)
print("," not in txt)

#3.

print("TERCER PUNTO")

x=0
for texto in txt:
    if texto == "i":
        x=x+1
print("i está presente en el texto", x ,"veces")

#4.

print("CUARTO PUNTO")

x=0
for texto in txt:
    if texto == " ":
        x=x+1
print("Los espacios está presente en el texto", x ,"veces")

#5.

print("QUINTO PUNTO")

x=0
for texto in txt:
    if texto == ",":
        x=x+1
print("Las , está presente en el texto", x ,"veces")

#6.



    

