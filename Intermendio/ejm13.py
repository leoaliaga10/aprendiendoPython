#Leer XML
#
import xml.sax
from xml.etree.ElementTree import parse

xml_doc = parse("ejemplo.xml")

for ele in xml_doc.findall('pro'):
	print (ele.text)