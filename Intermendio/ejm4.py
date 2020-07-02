#introspeccion
#la utilizamos para saber todas las instancias y propiedades del objeto
class Intro():
	Introver = 9
	def __init__(self,valor):
		self.valor = valor
	def segundo():
		print("Segundo")
	def tercero():
		print("tercero")	

dato = Intro("Valor")
dir(dato)

print(dir(dato))

#Si esta variable dato es instancia de la clase Intro
print(isinstance(dato,Intro))
#Si esta clase dato puede acceder al atributo
print(hasattr(dato,"Introver"))