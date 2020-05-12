#Ejemplo de archivos

def crearArchivo():
    archivo = open ('datos.txt','w')
    archivo.close()
def escribirArchivo():
    archivo = open ('datos.txt','a')
    archivo.write('Leoncio Aliaga\n')
    archivo.write('99912312')
    archivo.close()
def leerArchivo():
    archivo = open('datos.txt','r')
    linea = archivo.readline()
    while(linea != ""):
        print(linea)
        linea = archivo.readline()
    archivo.close()
leerArchivo()
