class clase():

    def __new__(cls):#sirve para personalizar
        print("new")
        return super().__new__(cls)#regresa una instancia,debo enviar la isntancia
    
    def __init__(self):#metodo especial por los dos guiones bajos
        #tareas de inicializacion el init
        print("init")
c=clase()
