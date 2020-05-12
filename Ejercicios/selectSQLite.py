#SQLITE
#SELECT
#
import sqlite3

conexion = sqlite3.connect("db_lite.sqlite")

print (conexion)

var = 'O'
query = "SELECT * FROM usuarios WHERE nombre LIKE '%" + var + "%'"
filas = conexion.execute(query)

#var = '1'
#filas = conexion.execute("SELECT * FROM 'usuarios' WHERE tipo=?",var) #CONSULTA SOLO PARA ENTEROS
conexion.commit()

lista = list()

for fila in filas:	
	#filas.fetchone() : Consulta solo un registro -el primero- separando cada valor de columna 
	#filas.fetchall() o filas : Consulta todos los registros en forma de tuplas
	#filas.fetchmany() : Consulta solo un registro -el primero- en forma de tupla
	lista.append(fila) #RESULTADOS COMO TUPLAS
	print fila

conexion.close()

print ("\n\nLISTA")
print (lista)

print ("\n\nLISTA ORDENADA")
lista.sort(key=lambda lista: lista[0])
print (lista)

print ("\n\nLONGITUD DE LISTA")
print (len(lista))
