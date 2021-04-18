#ejercicio 4
import re
texto = " Realizaunprogramaqueencuentreuna_palabra_unidaaotraconunguionbajo"
palabra_a_buscar = re.findall("[_]*",texto)
print(palabra_a_buscar)

