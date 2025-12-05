from random import randint
tam = randint(1,10)
vMin = randint(1,10)
vMax = randint(10,40) 
lista = [randint(vMin,vMax) for _ in range(tam)]
def maiorValor(lista):
    if not lista:
        return "Lista Vazia"
    elif len(lista) == 1:
        return lista[0]
    maior = lista[0]
    maior2 = maiorValor(lista[1:])
    if maior > maior2:
        return maior
    else:
        return maior2
print(lista)
print(maiorValor(lista))
    
    
    