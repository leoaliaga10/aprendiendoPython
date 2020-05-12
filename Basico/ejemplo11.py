#Ejemplo de clases POO
class Persona:
    nBrazos = 0
    nPiernas = 0
    cabello = True
    cCabello = "Gris"
    def __init__(self): #funcion indispensable
        self.nBrazos = 2
        self.nPiernas = 2
    def Dormir():
        pass            #para dejar vacia
    def Comer(self):
        self.hambre = 'Tengo hambre'
class Hombre(Persona):
    nombre = "Sin asignar"
    sexo = "M"
    def cambiarNombre(self,nombre):
        self.nombre= nombre
class Mujer(Persona):
    nombre = "Sin asignar"
    sexo = "F"

jose = Hombre()

jose.Comer()
jose.cambiarNombre("Leoncio")
print(jose.nombre)
