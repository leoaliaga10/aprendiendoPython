#ORDENAMIENTO
print('\n' *100)

lista = [9,1,3,6,7,4,2,5,0,9]

print(lista)
print(sorted(lista,reverse=True))

lista.sort()
print(lista)

lista2 = ['Za','Fg','Az','Ij']
print(sorted(lista2))
lista2.sort()
print(lista2)

#CONJUNTOS
print("CONJUNTOS")
conjunto = set('8923')
conjunto2 = {'1','3','7'}
print(conjunto)
print(conjunto2)
print("INTERSECCION")
print(conjunto & conjunto2)
print(conjunto.intersection(conjunto2))