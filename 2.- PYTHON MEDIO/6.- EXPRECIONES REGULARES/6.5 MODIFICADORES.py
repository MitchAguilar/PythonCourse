import re

regex=re.compile(r"ab",re.IGNORECASE)#con el ignore es para que no tenga en cuenta las mayussculas o minusculas

regex.search("sdjsndjAbskdss")

print(regex.search("sdjsndjAbskdss"))#muy imprecioannte
