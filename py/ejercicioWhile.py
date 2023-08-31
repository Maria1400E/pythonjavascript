polizaSalud = []
ingresoEstrato = 0
ingresSalario = 0
sumaLista = 0
promedioSub = 0
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0

while True:
    print("ingrese una opcion")
    print("opcion 1: ingresar nuevo asociado")
    print("opcion 2: generar resumen")
    print("opcion 3: salir")
    personas = int(input("Escriba su opcion: "))

    if personas == 1:
        ingresoEstrato = int(input("Ingrese el estrato de la persona: "))
        ingresSalario = int(input("Ingrese el salario de la persona: "))
        poliza = ingresSalario * 0.05
        if ingresoEstrato == 1:
            valorSubsidio = poliza * 0.50
            print("El valor de su poliza es de: ", poliza)
            print("El valor Subsidiado por el fondo es: ", valorSubsidio)
            print("El valor que debe cubrir el asociado es: ", poliza - valorSubsidio)
            polizaSalud.append(valorSubsidio)
            contador1 += 1
        if ingresoEstrato == 2:
            valorSubsidio = poliza * 0.40
            print("El valor de su poliza es de: ", poliza)
            print("El valor Subsidiado por el fondo es: ", valorSubsidio)
            print("El valor que debe cubrir el asociado es: ", poliza - valorSubsidio)
            polizaSalud.append(valorSubsidio)
            contador2 += 1
        if ingresoEstrato == 3:
            valorSubsidio = poliza * 0.30
            print("El valor de su poliza es de: ", poliza)
            print("El valor Subsidiado por el fondo es: ", valorSubsidio)
            print("El valor que debe cubrir el asociado es: ", poliza - valorSubsidio)
            polizaSalud.append(valorSubsidio)
            contador3 += 1
        if ingresoEstrato == 4:
            valorSubsidio = poliza * 0.20
            print("El valor de su poliza es de: ", poliza)
            print("El valor Subsidiado por el fondo es: ", valorSubsidio)
            print("El valor que debe cubrir el asociado es: ", poliza - valorSubsidio)
            polizaSalud.append(valorSubsidio)
            contador4 += 1
        if ingresoEstrato > 4:
           valorSubsidio = poliza * 0.10
           print("El valor de su poliza es de: ", poliza)
           print("El valor Subsidiado por el fondo es: ", valorSubsidio)
           print("El valor que debe cubrir el asociado es: ", poliza - valorSubsidio)
           polizaSalud.append(valorSubsidio)
           contador5 += 1
        print(polizaSalud)
    
    if personas == 2:
        sumaLista = sum(polizaSalud)
        promedioSub = sumaLista / len(polizaSalud)

        print("-------------------------------")
        print("RESUMEN")
        print("-------------------------------")
        print("Del estrato 1 hay", contador1,"inscritos")
        print("Del estrato 2 hay", contador2,"inscritos")
        print("Del estrato 3 hay", contador3,"inscritos")
        print("Del estrato 4 hay", contador4,"inscritos")
        print("De otro estrato hay", contador5,"inscritos")
        print("-------------------------------")
        print("El total desembolsado por el subsidio es: ", sumaLista)
        print("El promedio subsidiado por asociado es de: ",promedioSub)
        print("-------------------------------")
        break
    
    if personas == 3:
        break


           


