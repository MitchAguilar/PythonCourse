def crearArchivo():
    archivo=open("archivo 7.2 .txt","w")#con w en mode de escritura
    archivo.close() #se debe cerrar
def escribirArchivo():
    archivo=open("archivo 7.2 .txt","a")#con a lo que hacemos es agregar
    archivo.write("\nhola putos\n")
    archivo.write("98767890")
    

#crearArchivo()
escribirArchivo()
