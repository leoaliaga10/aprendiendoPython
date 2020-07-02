#Ejemplo de polimorfismo
class Perro:
	def avanzar(self):
		print("Corre")
class Perico:
	def avanzar(self):
		print("Volar")

def mover(animal):
	animal.avanzar()

perro = Perro()
perico= Perico()

perro.avanzar()
perico.avanzar()

#llamando a metodo generico

mover(perro)
mover(perico)

