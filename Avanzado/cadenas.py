#CADENAS
print('\n' *100)

cadena = " Hola Leoncio ? Pedro ? Miguel ? Jorge Luis" 

nueva = cadena.replace('Hola','HOLA') #Reemplaza una cadena por otra

nueva2 = cadena.strip() # Elimina espacios en clando

nueva3 = cadena.lstrip()

nueva4 = cadena.rstrip()

ma = cadena.upper() # cambia cadena a mayusculas

mi = cadena.lower() # cambia cadena a minusculas

print(nueva)
print(cadena.find("l")) #Busca una cadena dentro de otra
print(nueva2)
print(nueva3)
print(nueva4)
print(ma)
print(mi)

print(cadena.split("?")) #genera una lista
