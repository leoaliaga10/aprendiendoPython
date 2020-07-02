#Ejemplo de clases para calcular el área del circulo
class Circulo:
	"""docstring for circulo"""
	def __init__(self, radio):
		self.radio = radio
	@property
	def area(self):
		pi = 3.141592
		return pi * (self.radio**2)
	

c = Circulo(10)
print(c.area)
		
