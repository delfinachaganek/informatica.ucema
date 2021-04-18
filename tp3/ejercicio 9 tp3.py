#ejercicio 9
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
#(String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")
import re
texto = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"
x = re.split("Hoy estuvimos trabajando con re (.*)\ en python ", texto)
for a in x:
    print(a)