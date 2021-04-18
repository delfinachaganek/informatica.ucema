#Escribí un programa que lea una cadena y devuelva un diccionario 
#con la cantidad de apariciones de cada carácter en la cadena (considerar que las
# mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter 
#"A" tiene 1 aparición y el carácter "a" también tiene 1).
#ejercicio 10 y 11

contadores = {}
cadena = input ("escribi una cadena")
for caracter in cadena:
    if caracter in contadores:
        contadores[caracter]+=1
    else:
        contadores[caracter]=1

for clave, valor in contadores.items():
    print(clave,valor)

import string, re

abc = list(string.ascii_uppercase)
abc += list(string.ascii_lowercase)
#print (abc)

dic = {}
dici={}
texto = "Hola como estas, que honda"
for i in abc:
    if len(re.findall(i,texto)) > 0:
        dic[i]=len(re.findall(i,texto))

print(dic)

for i in abc:
    dici[i]=len(re.findall(i,texto))

print(dici)
