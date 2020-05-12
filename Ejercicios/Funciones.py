#PROGRAMACION FUNCIONAL
def saludar(lang):
  def saludar_es():
    print ("Hola")
  def saludar_en():
    print ("Hi")
  def saludar_fr():
    print ("Salut")
  lang_func = {"es": saludar_es,
  "en": saludar_en,
  "fr": saludar_fr}
  return lang_func[lang]

#OPCION 1
f = saludar("es")
f()

#OPCION 2
saludar("en")()

#FUNCION MAP
# 
print ("+++ FUNCION MAP")
def cuadrado(n):
  return n ** 2

l = [1, 2, 3]
l2 = map(cuadrado, l)
print (l2)

#FUNCION FILTER
#
print ("+++ FUNCION FILTER")
def es_par(n):
  return (n % 2.0 == 0)

l = [1, 2, 3]
l2 = filter(es_par, l)
print (l2)

#FUNCION REDUCE
#
print ("+++ FUNCION REDUCE")
def sumar(x, y):
  return x + y

l = [1, 2, 3]
l2 = reduce(sumar, l)
print (l2)

#FUNCION LAMBDA
#
print ("+++ FUNCION LAMBDA - ANONIMAS")
l = [1, 2, 3]
l2 = filter(lambda n: n % 2.0 == 0, l)
print (l2)
