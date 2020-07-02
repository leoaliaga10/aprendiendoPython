#closures manda valores a una funcion 
def funcionA(x):
	def funcionB(y):
		return x + y
	return funcionB

f = funcionA(5)
print (f(3)) #se asume q este es el segundo valor

#decorador: me permite modificar el comporatamiento de la funcion sin modificar su codigo
def PrimerD(funcion):
	def funcionDecorada(*args,**kkwars):
		print("Primer decoraror")
	return funcionDecorada

@PrimerD
def funcion():
	print("Mi primer decorador")

funcion()