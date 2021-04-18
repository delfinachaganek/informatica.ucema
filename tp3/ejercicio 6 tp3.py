#ejericicio 6
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.
import re
lista = ["hola", "chau", "pan", "bolso"]
frase = "Hoy como estas, tengo pan en el bolso, chau. "

for i in lista:
    patron = i
    if re.search(patron, frase) is not None:
        print("la palabra se encuentra en la lista dada")
    else:
        print("la palabra no se encuentra en la lista dada")