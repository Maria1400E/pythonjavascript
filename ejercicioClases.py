class autor:
    nombre =""
    hojas = 0
    libro = ""
    dinero = 0
    def __init__(self,nombre,hojas,libro,dinero):
        self.nombre = nombre
        self.hojas = hojas
        self.libro = libro
        self.dinero = dinero
    def escribir(self,tema):
        self.libro = tema

class editor:
    marca = ""
    publicacion = 0
    precioxHoja = 0
    def __init__(self,marca,publicacion,precioxHoja):
        self.marca = marca
        self.publicacion = publicacion
        self.precioxHoja = precioxHoja
    def imprimir(texto):
        print(texto)
    def cobrar(self,hojas):
        return self.precioxHoja * hojas
    
rafa = autor("Rafael pombo",32,"Mi pobre viejecita",25000)
norma = editor("Norma",1854,1500)

rafa.escribir("Erase una pobre viejecita sin nadita que comer")

norma.imprimir(rafa.libro)
norma.cobrar(1500)

    