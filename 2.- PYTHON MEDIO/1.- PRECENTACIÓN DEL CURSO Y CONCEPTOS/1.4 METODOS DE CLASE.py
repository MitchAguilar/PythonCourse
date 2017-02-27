class persona():
    def __init__(self):
        pass

    def despedir(self):
        print("adios")

    @classmethod#debe ponerce el decorador
    def saludar(cls,nombre):#necesitamos el cls
        print("Estoy saludando "+nombre)

persona.saludar("Mitch")# y no necesitamos crear metodo de clase
