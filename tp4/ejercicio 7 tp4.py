path = (r'C:\Users\usuario\Documents\python\suerte.txt')
lista1 = []
lista2 = []
with open(path,'r') as file:
    for lineas in file:
        lista1.extend(lineas.split())
    print("Hay", len(lista1), "palabras")
    for i in range(len(lista1)):
        lista2.append(len(lista1[i]))
    print(lista2)
    print(max(lista2))
    numero = lista2.index(7)
    print(lista1[numero])

import re
path = (r'C:\Users\usuario\Documents\python\suerte.txt')
lista1 = []
lista2 = []
with open(path,'r') as file:
    patron = "*\W"
    print(re.sub(patron," ", file))