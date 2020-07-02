#capturar excepciones
lista = [2,4]

try: 
	print(lista[1])
except IndexError:
	print("Error: error en el indice")
else:
	print("no hay error")
finally:
	print("Se ejecuto")

#lanzar excepcion
try:
	raise TypeError
except:
	print("Errores con los tipos")

#definir excepciones

class Err(Exception):
	def __init__(self, valor):
		print("Fue el error por: ", valor)

try:
	raise Err(4)
except Err: 
	print("Error escrito: ")

