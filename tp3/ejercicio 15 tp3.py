#ejercicio 15
import re
mail = input("Ingrese una direccion de mail:")
patron = "(\W|^)[\w.\-][^(()<>@,;:%]*((@)((gmail|hotmail|yahoo)\.com){1})(\W|$)"

if re.search(patron, mail) is not None:
    print("La direccion de mail es valida")
else:
    print("La direccion de mail no es valida")