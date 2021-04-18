#ejercicio 3
#Creá un programa que verifique las siguientes condiciones:

#si un string dado tiene una h seguida de ninguna o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de una o más e.

#si un string dado tiene una h seguida de dos o tres e.

import re
texto= "Hola como estas. Bien y vos! hermoso, Que bueno que estas acá"
patron= ('he*')
if re.search(patron, texto) is not None:
    print ("existe", patron)
else:
    print ("no existe")



patron= ('h' 'e' 'e')
if re.findall(patron, texto):
    print ("existe", patron)
else:
    print ("no existe")
