#ejercicio 7
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, 
#mayúsculas, espacios y números.
import re
lista = ["Cat 100", "---200", "xxxyyy", "jjj", "box4000", "tent500"]
for i in lista:
    x = re.match("^\d^\s[^a-zA-Z]", i)
if(x!=None):
	print("El texto no cumple con la condicion")
else:
	print("El texto cumple con la condicion")