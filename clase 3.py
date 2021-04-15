#ejercicio 2. poner la 4 y 5  letra de la palabra
str= input ("insertar string de minimo 6 letras")
if len(str) >= 6:
    print (str[4])
    print (str[5])
else:
    print("error, escribi minimo 6 letras")

#ejercicio 3. pedir nombre y saludar. 
nombre = input ("insertar y apellido nombre")
print ("Hola!", nombre) 

#ejercicio 4. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
nombre = input ("insertar nombre")
apellido1= input ("insertar apellido 1")
apellido2= input ("insertar apellido 2")
print (nombre[0].upper())
print (apellido1[0].upper())
print (apellido2[0].upper())
#el corchete y 0 funcionan para poner la letra que pide. 0 sería la letra 1.
#si no se ponen corchetes te pone la palabra entera
# upper es para que sea en mayuscula

#ejercio 5 Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
n1= input ("poner numero 1")
n2= input ("poner numero 2")
n3= input ("poner numero 3")
promedio= 

