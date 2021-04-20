path = (r'C:\Users\usuario\Documents\python\texto_suerte_echada.txt')
contador = 0
def texto (archivo):
    with open (archivo, 'r') as file:
        for i in file:
            if i[0] !="p":
                contador +=1

print("La cantidad de líneas que no empiezan con P son:", contador)

texto = (path)