#8
import re
path = (r'C:\Users\usuario\Documents\python\suerte.txt')
path2 = r'C:\Users\usuario\Documents\python\boquita.txt'
path3 = r'C:\Users\usuario\Documents\python\path3tp4.txt'

def combinar_archivos(path, path2, path3):
    with open(path, 'r') as file, open(path2, 'r') as file2, open(path3, 'w') as file3:
        for l1, l2 in zip(file, file2):
            file3.write(l1)
            file3.write('\n')
            file3.write(l2)
      
combinar_archivos(path, path2, path3)