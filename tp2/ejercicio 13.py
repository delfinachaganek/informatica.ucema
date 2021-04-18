#ejercico 13
def esMultiplo (n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

n1 = int(input("Insertar numero1"))
n2 = int(input("Insertar numero2"))

if esMultiplo(n1, n2):
 print(n1," es multiplo de ", n2)
else:
 print(n1," no es multiplo de ", n2)