import csv

doc=open("archivo2.csv","w")#con w es crear o escribir

doc_csv_w=csv.writer(doc)

lista=[["MITCH",999836],["uno",1000],["dos",33343],["tres",2323],["cuatro",1212]]

#doc_csv_w.writerows(lista)#ojo cambia la s

for x in lista:
    doc_csv_w.writerow(x)

doc.close()
