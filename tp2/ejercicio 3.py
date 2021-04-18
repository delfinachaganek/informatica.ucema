#Ej 3
# Escribí un programa que dado un número del 1 al 6,
# ingresado por teclado, muestre cuál es el número que está
# en la cara opuesta de un dado. Si el número es menor a 1
# y mayor a 6 se debe mostrar un mensaje indicando que es 
# incorrecto el número ingresado.
numero= int(input ("insertar numero del 1 al 6"))
if numero == 1:
     print ("6")
elif numero == 2:
    print ("5")
elif numero == 3:
    print ("4")
elif numero == 6:
    print ("1")
elif numero == 5:
    print ("2")
elif numero == 3:
    print ("4")
else:
    print("su numero ingresado es incorrecto")
