path = r'C:\Users\usuario\Documents\python\suerte.txt'
lista = []
with open (path,'r') as file:
    for i in range(14):
        lista.append(file.readline(i))
print(len(lista))
def imprimir_ul(n):
    print(lista[(6-n):])

imprimir_ul(2)
