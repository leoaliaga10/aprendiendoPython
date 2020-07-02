import json

with open('note.json') as archivo:
	dato = json.load(archivo)

print(dato)
print(dato['ClientesA'])