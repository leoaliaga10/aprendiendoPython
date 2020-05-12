#CADENAS
cadena = "Vamos Peru que tu puedes ganar"

valor = cadena.count("Peru",1,5)
print (valor)

valor = cadena.find("Peru")
print (valor)

s = " - "
secuencia = ("a", "b", "c")
valor = s.join(secuencia)
print (valor)

valor = valor.partition(s)
print (valor)

valor = cadena.replace("Peru","Cajamarca")
print (valor)

s = " "
valor = cadena.split(s)
print (valor)

valor = cadena.split(s,3)
print (valor)
