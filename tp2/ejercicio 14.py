#ejercicio 14
#Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
#Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima 
#y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van
#a introducir.

def temperatura_media(temperatura, temperatura1):
    return (temperatura+temperatura1)/2

dias= int(input("ingrese cantidad de días"))
num= 0

while num< dias:
    num +=1
    max= float(input("ingrese temperatura max del dia"))
    min= float(input("ingrese la temperatura min del dia"))
    print(temperatura_media(max,min))
