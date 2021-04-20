path = (r'C:\Users\usuario\Documents\python\suerte.txt')
with open (path,'r') as file:
    texto = file.read()
    palabras = texto.split()
    print(len(palabras))
    print(palabras)
