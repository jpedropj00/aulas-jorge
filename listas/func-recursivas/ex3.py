#contar elementos na lista
from random import randint
tam = randint(1,10)
vMin = randint(1,10)
vMax = randint(10,40) 
lista = [randint(vMin,vMax) for _ in range(tam)]
def contElementos(lista):
    if not lista:
        return 0
    return 1 + contElementos(lista[1:])
print(lista)
print(contElementos(lista))
    
