from functools import reduce
numeros = (1,2,3,4)
def suma(x,y):
	return x+y

sumar = reduce(suma,numeros)

print(sumar)