import re

re.search(r"k","kilometro")
print(re.search(r"k","kilometro"))
print(re.search(r"\d\d\d","kilo912metro"))#imprecionante
patron=re.compile("\d\d\d")
print(patron.search("kilo912metro").group())

if(re.search("\Aa[0-9].*(end|fin)$","a4 es una marca de fin")):#super wao!!!
    print("se encontró el patrón")
