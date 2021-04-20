path = (r'C:\Users\usuario\Documents\python\suerte.txt')
from itertools import islice
n = 5
with open (path,'r') as file:
    for i in islice(file, n):
        print(i)