import zipfile
from zipfile import ZipFile
with zipfile.ZipFile('archivo.zip','w') as fzip:
    fzip.write('note.json')
    fzip.write('archivo.xml')
    fzip.printdir()#me los muestra
    fzip.extracall()#para descomprimir
