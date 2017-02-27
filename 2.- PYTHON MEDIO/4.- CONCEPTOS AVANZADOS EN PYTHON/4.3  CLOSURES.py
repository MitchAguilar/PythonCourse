def funcionA(x):
    def funcionB(y):
        return x+y
    return funcionB

funcion=funcionA(5)#el primer valor es de la primera variable
print(funcion(3))#el segundo es de la segunda variable
