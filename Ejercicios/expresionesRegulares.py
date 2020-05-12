#expresiones regulares
import re

#	"\d”: un dígito. Equivale a [0-9]
#	“\D”: cualquier carácter que no sea un dígito. Equivale a [^0-9]
#	“\w”: cualquier caracter alfanumérico. Equivale a [a-zA-Z0-9_]
#	“\W”: cualquier carácter no alfanumérico. Equivale a [^a-zA-Z0-9_]
#	“\s”: cualquier carácter en blanco. Equivale a [ \t\n\r\f\v]
#	“\S”: cualquier carácter que no sea un espacio en blanco. Equivale a[^ \t\n\r\f\v]

#Sustitución
numero_sustituciones = 4
var = re.sub(r"\D","*","M12a3nge90ra1",numero_sustituciones)

print (var)
#Modificadores

var2 = re.compile(r"le",re.IGNORECASE)
salida = var2.search("LeoncioAliagaSaldaña")
print (salida)
print (var2.search("LeoncioAliagaSaldaña"))