'''
1) Desarrolle un programa que pida cinco notas de un estudiante, al final debe
    mostrar el promedio (usando while)
'''

while True:
    print()
    nombre = input("Ingrese el nombre del estudiante: ")
    notasEstudiantes = {"Nombre": nombre,"Notas":[]}
    cantNotas = 5
    for x in range(0,cantNotas):
        notas = float(input("nota {}: Ingrese las notas del estudiante: ".format(x)))
        notasEstudiantes["Notas"].append(notas)
        sumaNotas = sum(notasEstudiantes["Notas"])
        promedioNotas = sumaNotas/cantNotas
    print()
    print("El promedio del estudiante ",notasEstudiantes["Nombre"], "es: ",promedioNotas)
    if promedioNotas > 3:
        print()
        print("El estudiante ",nombre," Pasó la materia")
    else:
        print()
        print("El estudiante ",nombre," Perdió la materia")
