import csv

doc=open("archivo2.csv","r")#r mode de lectura, a, es concatenar
doc_csv=csv.reader(doc)

for (nombre,numero) in doc_csv:
    print nombre,numero

doc.close()
