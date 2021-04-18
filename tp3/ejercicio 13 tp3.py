#ejercicio 13
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.
import re
texto = "hola como estas, soy delfina. Que bueno, hola y chau."
x = re.sub("\W{1}","-",texto)
print(x)


