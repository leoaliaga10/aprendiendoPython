#Clase para asignar (SET) un dia y obtener (GET) el dia 
class Fecha():
  def __init__(self):
    self.__dia = 1
  def getDia(self):
    return self.__dia
  def setDia(self, dia):
    if dia > 0 and dia < 31:
      self.__dia = dia      
    else:
      print ("Error")

mi_fecha = Fecha()
mi_fecha.setDia(11)
variable = mi_fecha.getDia()
print (variable)
