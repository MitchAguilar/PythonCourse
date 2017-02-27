#numero= 5
class persona():
    edad=18#variable de clase, en forma general
    def __init__(self,nombre,nacionalidad):
        self.nombre= nombre
        self.nacionalidad= nacionalidad

persona1= persona("Mitch","Colombiano")

print(persona.edad)#si nos damos cuenta no creamos objeto
print(persona1.nombre)#variable de instancia
