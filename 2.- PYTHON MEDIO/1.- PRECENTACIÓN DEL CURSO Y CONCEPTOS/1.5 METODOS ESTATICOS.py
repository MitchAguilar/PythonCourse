class persona():

    def __init__(self):
        pass

    def brincar(self):
        print("brinco")

    @classmethod#debemos poner el decoradoer, es el equivalente al static en java
    def correr(cls):#se debe poner el cls
        print("corro")
    @staticmethod
    def nadar():
        print("nado")

mitch= persona()

mitch.nadar()
