# MANEJO DE DICCIONARIOS
# 
punto = {'x': 2, 'y': 1, 'z': 4}
materias = {}
materias["lunes"] = [6104, 7544]
materias["martes"] = [6201]
materias["miercoles"] = [6103, 7540]
materias["jueves"] = [6100, ["1A", "1B", "1C"]]
materias["viernes"] = [6201]
materias["sabado"] = [6501]

print("\n+++LONGITUD")
print (len(materias))
valor = materias["jueves"]
print (valor)
for x in valor:
	print x
valor = materias.get('luness',['No encontrado'])
print valor
print("\n+++BUSCAMOS VALOR")
valor = materias.has_key("martes")
print valor
print("\n+++ITEMS valores en TUPLAS")
valor = materias.items()
print valor
for x in valor:
	print x
print("\n+++KEYS")
valor = materias.keys()
print valor
print("\n+++VALUES")
valor = materias.values()
print valor

print("\n+++COPIA DE DIC")

copia_materias = materias.copy()
valor = copia_materias.items()
print valor

print("\n+++DIC VACIO")

copia_materias.clear()
valor = copia_materias.items()
print valor

print("\n+++ELEMENTOS DE UN DIC A DIC2")
materias.update(punto)
valor = materias.items()
print valor

print("\n+++VIERNES")
valor = materias.get("viernes")
print valor

print("\n+++NUEVO ELEMENTO")
materias["Domingo"] = [6000, 7000]
valor = materias.items()
print valor

# Insertamos un elemento en el array. Si la clave ya existe no inserta el elemento
print("\n+++NUEVO ELEMENTO SI LA CLAVE EXISTE NO INSERTA NADA")
valor = materias.setdefault("Lunes2",[0000])
print materias

print("\n+++ELIMINAR KEY")
materias.pop("Lunes2")
print materias

# Creamos un diccionario a partir de una lista con las claves
print("\n+++CREAMOS UN DICIONARIO A PARTIR DE UNA LISTA")
keys = ['nombre', 'apellidos', 'edad']
dicionario = dict.fromkeys(keys,"Vacio")

print dicionario
