class persona:#no se pueden crear vacias cuidado con pass
    Nbrazos=0
    Npiernas=0
    cabello=True
    Ccabello="defecto"
    hambre=0

    def __init__(self):#constructor para inicializar
        self.Nbrazos=2
        self.Npiernas=2

    
    def dormir():
        pass
    def comer(self):#me hago referencia a mi mismo
        self.hambre=455555555543


        
class hombre(persona):#con solo ésto tenemos la herencia
    nombre="defecto"
    sexo="M"
    def cambiarNombre(nombre):#nombre es por yo solito y que em entra
        self.nombre=nombre



class mujer(persona):
    nombre="efecto"
    sexo="Putito"





jose=hombre()
jose.comer()

print(jose.hambre)
