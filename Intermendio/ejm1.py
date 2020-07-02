#Ejemplo de clases
class Persona():
	edad = 18

	def __init__(self, nombre, nacionalidad):
		self.nombre = nombre
		self.nacionalidad = nacionalidad
		print("init")

	def nadar(self):
		print("Estoy nadando")

	@classmethod
	def saludar(cls, nombre):
		print("Estoy saludando : " + nombre)

	@classmethod
	def correr(cls):
		print("Estoy corriendo")

class Clase():
    #metodos especiales
	#personaliza clases
	def __new__(cls):
	 	print("new")
	 	return super().__new__(cls)

	def __init__(self):
		print("init")
persona1 = Persona("Leoncio","Peruano")

#Utilizo la variable de clase
print(Persona.edad)

#metodo de instancia
print(persona1.nombre)

#metodo de instancia
persona1.nadar()

#metodo de clase
Persona.saludar("Leo")

#metodo estatico
jose = Persona("Jose","De los palotes")
jose. correr()

#metodos especiales
c = Clase()
