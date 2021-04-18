#ejercico 5
import re
texto1 = "2 personas caminando"
patron = int(input("insertar numero"))
def coincide(texto1, patron):
    if re.match (texto1, patron):
       print ("coincidencia")
    else: 
        print ("no coincide")