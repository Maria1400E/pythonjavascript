class vehiculo:
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
    def caracteristicas(self):
        return super().caracteristicas() + ", {} descapotable".format(self.descapotable)
    

class camioneta(vehiculo):
    def __init__(self, dueño, puertas, ruedas, tara, carga):
       super().__init__(dueño, puertas, ruedas)
       self.tara = tara
       self.carga = carga
    def caracteristicas(self):
        return super().caracteristicas() + ", {} kilos".format(self.carga)


b = camioneta("Camilo", 4, 4, 43.8, 67)
c = auto("Esteban", 2, 4, True)
print(b.caracteristicas())
print(c.caracteristicas())
