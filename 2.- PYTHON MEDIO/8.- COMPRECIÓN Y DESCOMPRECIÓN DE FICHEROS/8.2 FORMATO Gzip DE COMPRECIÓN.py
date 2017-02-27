import gzip
with open('archivo.xml','rb') as original:
    with gzip.open('archivo.txt.gz','wb') as archivo1:
        archivo1.writelines(original)

