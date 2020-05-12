import csv

doc = open("archivo.csv","w")

doc_csv_w = csv.writer(doc)

lista = [["Pedro",947732087],["Pedro",947732087],["Pedro",947732087],["Pedro",947732087],["Pedro",947732087],["Pedro",947732087]]

for x in lista:
	doc_csv_w.writerow(x)	#escribe linea a linea

#doc_csv_w.writerows(lista)

doc.close()
