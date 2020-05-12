#Ejemplo de listas
lista = ['Leo','Maria','20','15']

longitud = len(lista)

for elementos in lista:
    print (elementos)

#unir listas
lista_nueva = ['Armando','Grecia','2','5']

lista_final = lista + lista_nueva

print(lista_final)

if (98 in lista):
    print("Si")
else:
    print("No")
#indice negativo
print(lista[-3])
