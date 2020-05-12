#Ordenar listas en Python, con ejemplos
#
#
# Lista de Tuplas
futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"), (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), (6, "Iniesta"), (7, "Villa")]

futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print ("\nImprimimos las lista ordenada por dorsal asc:")
print (futbolistasTup)

futbolistasTup.sort(key=lambda futbolista: futbolista[0], reverse=True)
print ("\nImprimimos las lista ordenada por dorsal desc:")
print (futbolistasTup)

futbolistasTup.sort(key=lambda futbolista: futbolista[1])
print ("\nImprimimos las lista ordenada por el nombre del jugador:")
print (futbolistasTup)

# Lista de Strings
futbolistas = ["1 - Casillas", "15 - Ramos", "3 - Pique", "5 - Puyol", "11 - Capdevila", "14 - Xabi Alonso", "16 - Busquets", "8 - Xavi Hernandez", "18 - Pedrito", "6 - Iniesta", "7 - Villa"]
futbolistas.sort(key=lambda futbolista: futbolista.split("-")[1], reverse=True)
print ("\nImprimimos las lista ordenada por el nombre del jugador desc:")
print (futbolistas)


class Futbolista():
	def __init__(self, dorsal, nombre, demarcacion):
		self.dorsal = dorsal
		self.nombre = nombre
		self.demarcacion = demarcacion

	def __str__(self):
		return "%i - %s - %s" % (self.dorsal, self.nombre, self.demarcacion)

#from Futbolista import Futbolista

futbolistasOb = Futbolista(0,'Leoncio','DT')

print ("\nOBJETO")
print (futbolistasOb.dorsal)
print (futbolistasOb.nombre)
print (futbolistasOb.demarcacion)

#vamos a realizar una lista con el objeto
futbolistasOb = list()
futbolistasOb.append(Futbolista(1,'Casillas','Portero'))
futbolistasOb.append(Futbolista(15,'Ramos','Lateral Derecho'))
futbolistasOb.append(Futbolista(3,'Pique','Central'))
futbolistasOb.append(Futbolista(5,'Puyol','Central'))
futbolistasOb.append(Futbolista(11,'Capdevila','Lateral Izquierdo'))
futbolistasOb.append(Futbolista(14,'Xabi Alonso','Medio Centro'))
futbolistasOb.append(Futbolista(16,'Busquets','Medio Centro'))
futbolistasOb.append(Futbolista(8,'Xavi Hernandez','Centro Campista'))
futbolistasOb.append(Futbolista(18,'Pedrito','Interior Izquierdo'))
futbolistasOb.append(Futbolista(6,'Iniesta','Interior Derecho'))
futbolistasOb.append(Futbolista(7,'Villa','Delantero'))

futbolistasOb.sort(key=lambda futbolista: futbolista.dorsal)
print ("\nFutbolistas ordenados por el atributo Dorsal")
for i in futbolistasOb:
    print (i)

futbolistasOb.sort(key=lambda futbolista: futbolista.nombre, reverse=True)
print ("\nFutbolistas ordenados descendentemente por el atributo Nombre")
for i in futbolistasOb:
    print (i)
