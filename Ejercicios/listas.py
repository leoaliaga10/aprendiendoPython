#Crear una lista:
mylist = ['one', 20, 5.5, [10, 15], 'five']
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[2] = "New item"

#Si el índice es negativo, cuenta desde el último elemento.
elem = mylist[-1]

# Recorrer una lista con un for:
for elem in mylist:
     print(elem)

#Actualizar elementos:
mylist = [1, 2, 3, 4, 5]
for i in range(len(mylist)):
    mylist[i]+=5
print(mylist)

#Cortar una lista:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist[1:3] = ['Hello', 'Seven']
print(mylist)

#Insertar en una lista:
mylist = [1, 2, 3, 4, 5]
mylist.insert(1, 'New')
print(mylist)

#Agregar a una lista al final:
mylist = ['one', 'two', 'three', 'four', 'five']
mylist.append("New")

#Juntas dos listas
mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ["New one", "New Two"]
mylist.extend(list2)
print(mylist)

#Ordenar una Lista:
mylist = ['cde', 'fgh', 'abc', 'klm', 'opq']
alist = [3, 5, 2, 4, 1]
mylist.sort()
alist.sort()
print(mylist)
print(alist)

#Invertir una lista:
mylist = [1, 2, 3, 4, 5]
mylist.reverse()
print(mylist)

#Indice de un elemento:
mylist = ['one', 'two', 'three', 'four', 'five']
print(mylist.index('two'))

#Eliminar un elemento por indice
mylist = ['one', 'two', 'three', 'four', 'five']
removed = mylist.pop(2)
print(mylist)
print(removed)

#Eliminar un elemento especifico
mylist.remove('two')

#Eliminar un elemento por indice
del mylist[2]

#Eliminar varios elementos por indice
mylist = ['one', 'two', 'three', 'four', 'five']
del mylist[1:3]
print(mylist)

#Funciones para listas
mylist = [5, 3, 2, 4, 1]
print(len(mylist))
print(min(mylist))
print(max(mylist))
print(sum(mylist))

#Comparar listas:
mylist = ['one', 'two', 'three', 'four', 'five']
list2 = ['four', 'one', 'two', 'five', 'three']
if (mylist == list2):
     print("Iguales")
else:
     print("Diferentes")

#Operaciones matematicas en las listas:
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list1 + list2)
print(list1 * 2)

#Convertir una cadena en lista
mystr = "LikeGeeks"
mylist = list(mystr)
print(mylist)

#Convertir una cadena con espacios en lista
mystr = "LikeGeeks"
mystr = "Welcome to likegeeks website"
mylist = mystr.split()
print(mylist)

#Unir una lista:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
delimiter = ' '
output = delimiter.join(mylist)
print(output)

#Aliasing:
mylist = ['Welcome', 'to', 'likegeeks', 'website']
list2 = mylist
list2[3] = "page"
print(mylist)

#clonar lista
mylist = ['Welcome', 'to', 'likegeeks', 'website']
myclone = list(mylist)
id(mylist)
id(myclone)