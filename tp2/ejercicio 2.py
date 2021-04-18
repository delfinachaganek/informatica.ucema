#ej 2 : Escribí un programa que pida un número y diga 
# si es positivo, negativo o 0 y además 
# informe si es par o impar (el 0 es un número par).
# falta poner si es par o inpar
numero = int(input("insertar número"))
if numero > 0 and numero % 2 == 0:
  print("positivo y par")
elif numero > 0 and numero % 2 != 0:
  print("positivo e impar")
elif numero < 0 and numero % 2 == 0:
  print("negativo y par")
elif numero < 0 and numero % 2 != 0:
  print("negativo e impar")
elif numero == 0:
  print("Es cero y par")