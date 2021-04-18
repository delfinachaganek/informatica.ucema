#ejercicio 12
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por 
#la barra vertical (|).
import re
texto = "hola como estas, soy delfina. Que bueno, hola y chau."
patron = ("[-]*\s")
print(re.sub(patron, "|", texto))
#nose como hacer para reeemplazar dos caracteres diferentes


