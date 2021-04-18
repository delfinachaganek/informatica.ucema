#4
gramos = int(input("ingresar peso en gramos"))
zona = input("ingresar zona")
if gramos < 5000:
    if zona == "america del sur":
        print(10 * gramos)
    if zona == "america central":
        print(15 * gramos)
    if zona == "america del norte":
        print(18 * gramos)
    if zona == "europa":
        print(24 * gramos)
    if zona == "asia":
        print(30 * gramos)
else:
    print("la entrega fue rechazada")