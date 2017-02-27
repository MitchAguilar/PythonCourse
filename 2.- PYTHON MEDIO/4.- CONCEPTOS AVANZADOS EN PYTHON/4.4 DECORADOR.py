def primerD(funcion):
    def funcionDecorada(*args,**kkwars):
        print("Primer Decorador")
    return funcionDecorada
@primerD
def funcion():
    print('Mi primer decorador')

funcion()

#modificar el comprtamiento de una función
#ejecute el codigo sopenco
