#COMPRENSION DE LISTAS
#
print ("+++ COMPRESION DE LISTAS")
print ("\n++++++++++++++++++++++++")
print ("\nPOTENCIA")
l = [1, 2, 3]
l2 = [n ** 2 for n in l]
print (l2)

print ("\nPARES")
l2 = [n for n in l if n % 2.0 == 0]
print l2

print ("\nVARIAS")
l = [0, 1, 2, 3]
m = ["a", "b"]
n = [s * v for s in m for v in l if v > 0]
print (n)