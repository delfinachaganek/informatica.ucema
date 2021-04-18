#1
#Escribí un programa que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.
import re
texto= "Hola como estas. Bien y vos! Que bueno que estas acá"
patron = "[a-zA-Z0-9]"
def programa_verificado (patron,texto):
    if re.search (patron,texto):
        print ("verificado")
    else: 
        print("no verificado")
programa_verificado (patron,texto)
