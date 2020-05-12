#SQLITE
#INSERT 
#
import sqlite3

conexion = sqlite3.connect("db_lite.sqlite")

print ("Conectado: ", conexion)

query = "INSERT INTO usuarios ('nombre','usuario','clave','tipo') VALUES ('LEILA','LSALDAÑA','A12241262',1)"

try:
	conexion.execute(query)
except: # (IntegrityError, NameError)
	print ("REGISTRO NO GUARDADO")
else:
	print ("REGISTRO GUARDADO")

conexion.commit()

conexion.close()