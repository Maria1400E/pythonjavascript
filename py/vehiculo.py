"""class vehiculo:
    def __init__ (self,dueño,puertas,ruedas):
        self.dueño = dueño
        self.puertas = puertas
        self.ruedas = ruedas
    def caracteristicas(self):
        return "Dueño {}, {} puertas, {} ruedas".format(self.dueño,self.puertas,self.ruedas)


class auto(vehiculo):
    def __init__(self, dueño, puertas, ruedas, descapotable):
        super().__init__(dueño, puertas, ruedas)
        self.descapotable = descapotable
    def esDescapo(self):
        if self.descapotable:
            return "Su vehivulo es descapotable"
        else:
            return "Su vehiculo no es descapotable"
    def caracteristicas(self):
        return super().caracteristicas() + ", {}".format(self.descapotable)
    

class camioneta(vehiculo):
    def __init__(self, dueño, puertas, ruedas, tara, carga):
       super().__init__(dueño, puertas, ruedas)
       self.tara = tara
       self.carga = carga
    def caracteristicas(self):
        return super().caracteristicas() + ", {} kilos de carga, {} kilos de tara".format(self.carga,self.tara)


b = camioneta("Camilo", 4, 4, 43.8, 67)
c = auto("Esteban", 2, 4, True)
print(b.caracteristicas())
print(c.caracteristicas())
print(c.esDescapo())"""

class Vehiculo():
    
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
        
    def __str__(self):
        return "color {}, {} ruedas".format( self.color, self.ruedas )
                
class Coche(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return "Este es un coche y sus caracteristicas son: " + super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

class bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return "Esta es una bicicleta y sus caracteristicas son: " + super().__str__() + ", tipo {}".format(self.tipo)

class camioneta(Vehiculo):
    def __init__(self, color, ruedas, carga):
        super().__init__(color, ruedas)
        self.carga = carga
    def __str__(self):
        return "Esta es una camioneta y sus caracteristicas son: " + super().          + ", carga {}".format(self.carga)
    
class motocicleta(Vehiculo):
    
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        
    def __str__(self):
        return "Esta es una motocicleta y sus caracteristicas son: " + super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

    
c = Coche("Azul", 4, 150, 1200)
b = bicicleta("Roja",2,"Urbana")
cm = camioneta("Negra",4,43.8)
m = motocicleta("Gris",2,300,660)
print(c)
print(b)
print(cm)
print(m)