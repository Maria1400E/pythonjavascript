class persona:
    nombreP=""
    apellidoP=""
    def __init__(this,nombre,apellido):
        this.nombreP=nombre
        this.apellidoP=apellido
p1 = persona("Juan","Perez")
print(p1.nombreP)


class animal:
    patas = 0
    habitad = ""
    familia = ""
    def __init__(this,patas,habitad,familia):
        this.patas=patas
        this.habitad=habitad
        this.familia=familia
tigre = animal(4,"Tierra","Felinos")
pajaro = animal(2,"Aire","Aves")
print(pajaro.patas)