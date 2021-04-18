nombres = []
edades = []

nom=input("ingrese un nombre")
if nom != "*":
    nombres.append(nom)
    edad=int(input("ingrese su edad"))
    edades.append(edad)
else:
    print("no hay alumnos")

while nom!="*":
    nom= input("ingrese un nombre")
    if nom!="*":
        nombres.append(nom)
        edad = int(input("ingrese su edad"))
        edades.append(edad)

edad_max = max(edades)

for i in range(len(edades)):
    if edades[i] == edad_max:
        print(nombres[i])