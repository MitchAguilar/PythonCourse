lista=[2,4]

try:
    print(lista[5])
except IndexError:
    print("Error: error en el indice")
else:
    print("no hay error")

finally:
    print("se ejecutó")
#mirar en el compilador para el error
