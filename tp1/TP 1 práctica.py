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
n1= int(input ("poner numero 1"))
n2= int(input ("poner numero 2"))
n3= int(input ("poner numero 3"))
suma = n1 +n2 + n3
promedio= suma/3
print("el promedio es:", promedio)

#ejercicio 6
#Dada una cierta cantidad de minutos (ingresada por teclado)
#hacer un programa que muestre cuántas horas y minutos son.
#Por ejemplo 150 minutos son 2 horas y 30 minutos.
minutos= int(input ("ingresar cantidad de minutos"))
horas= minutos/60
print("son", horas, "horas")

#ejercicio 7
#Un comerciante, el cual tiene un sueldo base, 
# recibe un 10% extra por comisión por cada venta
# que realiza. Realizar un programa que devuelva el dinero 
# que recibirá por comisión luego de 4 ventas y el total de 
# dinero que ganará ese mes, teniendo en cuenta estas ventas 
# y su sueldo base.

sueldo_base = int(input("ingrese sueldo base"))
venta1 = int(input("ingrese primera ganancia"))
venta2 = int(input("ingrese segunda ganancia"))
venta3 = int(input("ingrese tercera ganancia"))
venta4 = int(input("ingrese cuarta ganancia"))
comisión = venta1*0.1 + venta2*0.1 + venta3*0.1 + + venta4*0.1
sueldo_total= sueldo_base + comisión
print("el sueldo total es", sueldo_total, ".")

#ejercicio 8
#Escribir un programa para calcular la nota final de un 
#estudiante, teniendo en cuenta que por cada respuesta 
#correcta el estudiante suma 4 puntos, por cada incorrecta 
#se le resta 1 punto y si la respuesta está en blanco no se
# le suma ni se le resta.
notas_correctas= int(input("cantidad de notas correctas"))
notas_incorrectas= int(input("cantidad de notas incorrectas"))
notas_en_blanco= int(input("cantidad de notas en blanco"))
nota1 = notas_correctas*4
nota2 = notas_incorrectas
nota_final = (nota1 - nota2)
print ("la nota final es", nota_final)


