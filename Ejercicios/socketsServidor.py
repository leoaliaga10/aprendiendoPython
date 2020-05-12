#SOCKETS
#SERVIDOR
import socket

try:
	socket_s = socket.socket()
except:
	print ("Problemas")
else:
	print ("Conexion")

socket_s.bind(("localhost", 9999))

socket_s.listen(1)
sc, addr = socket_s.accept()
#socket_c,(host_c, puerto_c) = socket_s.accept()

while True:
	recibido = sc.recv(1024)
	if recibido == "quit":
		break
	print ("Recibido:", recibido)
	sc.send(recibido)

print ("adios")
sc.close()
socket_s.close()