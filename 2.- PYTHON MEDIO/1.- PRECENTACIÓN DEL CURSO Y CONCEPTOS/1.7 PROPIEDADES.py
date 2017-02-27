class circulo:

    def __init__(self,radio):
        self.radio=radio

    @property#propiedad 
    def area(self):
        return 3.1416*(self.radio**2)

c=circulo(10)

print(c.area)#accedio como propiedad no como metodo
