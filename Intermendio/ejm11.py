#busqueda de patrones

import re 

print(re.search(r"k","Kilometro"))

print(re.search(r"\d\d\d","Kilo911metro"))

patron = re.compile("\d\d\d")

print(patron.search("Kilo123metro").group())

if (re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):
	print("Se encontro el patron")

#Sustituciones

print(re.sub(r"\d","*","Mpaneg8ra990",2))

#modificadores

regex = re.compile(r"ab",re.IGNORECASE)
print(regex.search("jauqnaBsAmATT"))