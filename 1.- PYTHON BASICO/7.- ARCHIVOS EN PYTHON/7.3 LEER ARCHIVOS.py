def crearArchivo():
    archivo=open("archivo 7.2 .txt","w")
    archivo.close() 
def escribirArchivo():
    archivo=open("archivo 7.2 .txt","a")
    archivo.write("\nhola putos\n")
    archivo.write("98767890")
    
def leerarchivo():
    archivo=open("archivo 7.3.txt","r")#leer en modeo de lectura
    linea=archivo.readline()
    while linea!="":
        print(linea)
        linea=archivo.readline()
    archivo.close()

leerarchivo()
