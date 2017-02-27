#def lower(elementos):return elementos.lower()

#lista=["Mitch","AguIlar","No"]


#print(list(map(lower,lista)))#ojo se liga map,filter,reduce.

#print([cad.lower() for cad in lista])

# FUNCIONES DEL ORDEN SUPERIOR

def saludo(idioma):
    def saludo_es():
        print("Hola")
    def saludo_en():
        print("HI")
    idioma_func={"es":saludo_es,
                 "en":saludo_en
                 }
    return idioma_func[idioma]
saludar=saludo("es")
saludar()
