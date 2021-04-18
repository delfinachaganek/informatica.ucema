#ejercicio 8
#Escribí un programa que separe y devuelva los caracteres númericos de un string.
import re
numeros = "3 hola como 4 estas a 7 que bueno 9!"
x = re.split("\D+", numeros)
for a in x:
    print( a)