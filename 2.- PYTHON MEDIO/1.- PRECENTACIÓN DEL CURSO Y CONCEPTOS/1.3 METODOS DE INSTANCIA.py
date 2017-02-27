class persona():
    edad=18
    def __init__(self,nombre,nacionalidad):
        self.nombre= nombre
        self.nacionalidad= nacionalidad

    def nadar(self):#metodo de instancia, debemos por obligacion colocar el self
        print("estoy nadando")

persona1= persona("Mitch","Colombiano")

persona1.nadar()#madnar a llamar un metodo
