#SOCKETS
#CLIENTE
import socket

socket_c = socket.socket()
socket_c.connect(("localhost", 9999))

while True:
	mensaje = input("> ")
	socket_c.send(mensaje)
	if mensaje == "quit":
		break

print ("adios")

socket_c.close()