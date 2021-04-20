#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings 
#están delimitadas por los caracteres @ o &.
#ejercicio 10
import re
texto = " Realiza @ unprograma que& encuentre una palabra unidaa otra conunguionbajo"
palabra_a_buscar = re.findall("@(.*)&",texto)
print(palabra_a_buscar)