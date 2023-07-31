"""Para una campaña de salud se requiere determinar de un
grupo de N personas cuantos pueden beneficiarse.
Serán beneficiarios quienes siendo mujeres no pasen
de 30 años y quienes siendo hombres no superen los 35 años.
La campaña es solo para estratos 1 y 2. Se debe mostrar:

a. Cuantos hombres son beneficiados
b. Cuantas mujeres son beneficiadas
c. Mostrar el promedio de edad de hombres beneficiados
d. Mostrar el promedio de edad de mujeres beneficiadas

Indicar mediante un mensaje cuando no se es beneficiado."""
persona = []
ingresoEdad = 0
ingresoEstrato = 0
ingresoGenero = 0
hombresBeneficiados = 0
mujeresBeneficiados = 0
sumaEdadMujeres = 0
sumaEdad = 0

cantidadPersonas = int(input("Escriba la cantidad de personas que se van a inscribir: "))

for x in range(1,cantidadPersonas):
    ingresoEdad = int(input("Ingrese la edad de la persona: "))
    ingresoGenero = input("Ingrese el genero de la persona (F/M): ")
    ingresoEstrato = int(input("Ingrese el estrato de la persona: "))
    persona.append({'edad':ingresoEdad,'genero':ingresoGenero,'estrato':ingresoEstrato})

    if (ingresoGenero == "M" and ingresoEdad <= 35 and ingresoEstrato in [1,2]):
        hombresBeneficiados += 1
        sumaEdad += ingresoEdad
        
    elif (ingresoGenero == "F" and ingresoEdad <= 30 and ingresoEstrato in [1,2]):
        mujeresBeneficiados += 1
        sumaEdadMujeres += ingresoEdad
        
    
if hombresBeneficiados > 0:
            promedioHombres = sumaEdad/hombresBeneficiados
            print("La cantidad de hombres beneficiados es: ",hombresBeneficiados)
            print("El promedio de edad de hombres beneficiados es:", promedioHombres)
else:
        print("No hay hombres beneficiados")

if mujeresBeneficiados > 0:
        promedioMujeres = sumaEdadMujeres/mujeresBeneficiados
        print("La cantidad de mujeres beneficiadas es: ",mujeresBeneficiados)
        print("El promedio de edad de mujeres beneficiadas es:", promedioMujeres)
else:
        print("No hay mujeres beneficiadas")


        



    
    
        
