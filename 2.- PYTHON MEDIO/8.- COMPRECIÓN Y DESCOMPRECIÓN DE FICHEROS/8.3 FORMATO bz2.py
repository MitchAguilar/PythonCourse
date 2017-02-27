import bz2

cadena=b"cadena cadena cadena cadena cadena"

cadena_c=bz2.compress(cadena)

print(cadena)#normal
print(cadena_c)#cadena comprimida
print(bz2.decompress(cadena_c))#normal
