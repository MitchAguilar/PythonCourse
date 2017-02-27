lista=["hola",4,3.3,"holi"]
lista2=["perro",2,2,2]
lista3=["hola",4,3.3,"holi","perro",2,2,2]
print(len(lista))#tamaño de la lista

for elemento in lista:
    print (elemento)

listaf=lista+lista2

print(listaf)

if 4 in lista:#si se encuentra
    print ('si se encuentra')

print(lista3[0:])
