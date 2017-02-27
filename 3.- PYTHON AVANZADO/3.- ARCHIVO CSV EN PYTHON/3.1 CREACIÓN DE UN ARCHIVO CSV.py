import csv

doc=open("archivo.csv","w")#con w es crear o escribir

doc_csv_w=csv.writer(doc)

lista=["MITCH",999836]

doc_csv_w.writerow(lista)

doc.close()
