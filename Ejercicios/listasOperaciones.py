# Declaramos una lista con diferente tipos de datos
listaEjemplo = [1, 3.1416, 'j', 'jarroba.com',  True]

print ('Imprimimos los elementos de una lista y el tipo de dato de cada elemento')
for l in listaEjemplo:
    print ('%s - %s' %(l, type(l)))

# Declaración de una lista
lista = list()

# Cuenta el número de elementos de la lista
valor = len(lista)
print (valor)

# Agrega un elemento (x) al final de la lista.
x = "Leoncio"
lista.append(x)
print (lista)

# Inserta un elemento (x) en una posición determinada (pos)
x = "Rosa"
lista.insert(0, x)
print (lista)

# Une dos listas (une la lista2 (la que se pasa como parámetro) a la lista)
# ########
lista2 = 'Valeria'
lista.extend(lista2)
print (lista)

# Borra el primer elemento de la lista cuyo valor sea x. Sino existe devuelve un error
x = "V"
lista.remove(x)
print (lista)

# Borra el elemento en la posición dada de la lista, y lo devuelve.
pos = 0
valor = lista.pop(pos)
print (valor)

# Borra todos los elementos de la lista (lista.clear())
del lista[:]
print (lista)


lista = ["a","u","e","o","i","a"]

# Devuelve el índice en la lista del primer elemento cuyo valor sea x.
x = "a"
valor = lista.index(x)
print (valor)

# Devuelve el número de veces que x aparece en la lista.
x = "a"
valor = lista.count(x)
print (valor)

# Ordena los ítems de la lista
lista.sort(cmp=None, key=None, reverse=False)
print (lista)

# Invierte los elementos de la lista.
lista.reverse()
print (lista)

# Devuelve una copia de la lista (lista.copy())
listaCopia = lista[:]
print (listaCopia)

print ("\n+++ DIVISION +++")

# Ejemplo de lista en la que guardaremos las demarcaciones en el fútbol
demarcaciones = list()

# Insertamos algunas demarcaciones
demarcaciones.append('Defensa')
demarcaciones.append('Lateral')
demarcaciones.append('MedioCentro')
demarcaciones.append('Centro Campista')
demarcaciones.append('Extremo')
print (demarcaciones)

# Insertamos elementos en posiciones determinadas
demarcaciones.insert(0, 'Portero')
demarcaciones.insert(6, 'Delantero')
print (demarcaciones)

# Concatenamos dos listas
lista2 = ['Arquero', 'Carrilero', 'Portero', 'Lateral']
demarcaciones.extend(lista2)
print (demarcaciones)

# Borramos la primera aparición del elemento 'Lateral' de la lista
demarcaciones.remove('Lateral')
print (demarcaciones)

# Borramos en tercer elemento de la lista PD: las lista empiezan en el elemento 0
demarcaciones.pop(2)
print (demarcaciones)

# Buscamos la posición del primer elemento con valor = 'Extremo'
print (demarcaciones.index('Extremo'))

# Vemos el número de veces que esta en la lista el elemento 'Portero' y 'Delantero'
print (demarcaciones.count('Portero'))
print (demarcaciones.count('Delantero'))

# Invertimos los elementos de las lista
demarcaciones.reverse()
print (demarcaciones)

# Hacemos una copia de la lista demarcaciones
copiaDemarcaciones = demarcaciones[:]
print ('Copia %s' %copiaDemarcaciones)

# Borramos todos los elementos de la lista 'copiaDemarcaciones'
del copiaDemarcaciones[:]
print (copiaDemarcaciones)

# Ordenamos la lista demarcaciones por orden alfabético
demarcaciones.sort()
print (demarcaciones)

demarcaciones.sort(reverse=True) #o mylist.reverse()
print (demarcaciones)














