import re
path = (r'C:\Users\usuario\Documents\python\suerte.txt')
path2 = r'C:\Users\usuario\Documents\python\boquita.txt'
with open(path, 'r') as file:
    texto = file.read()
    with open(path2, 'a') as file2:
         file2.write(re.sub("\n","",texto))

