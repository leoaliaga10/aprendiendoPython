def lower(elementos):return elementos.lower()

lista = ["LEONCIO","ALIAGA SALDAÑA","Peruano"]
print(list(map(lower, lista)))

print([cad.lower() for cad in lista ])

#--------------------------------
def saludo(idioma):
	def saludo_es():
		print("Hola")
	def saludo_en():
		print("Hello")
	idioma_func = {"es":saludo_es,
					"en":saludo_en
					}
	return idioma_func[idioma]

saludar = saludo("en")
saludar()