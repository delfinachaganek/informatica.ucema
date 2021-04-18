#ejercicio 14
import re
texto = "hola como estas, soy delfina. Que bueno, hola y chau."
patron = ("\s")
print(re.sub(patron, ";", texto)) 