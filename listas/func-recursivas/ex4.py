from random import randint
tam = randint(1,10)
vMin = randint(1,10)
vMax = randint(10,40) 
lista = [randint(vMin,vMax) for _ in range(tam)]
def somar_lista(lista):
    if not lista:
        return 0
    return lista[0] + somar_lista(lista[1:])
print(lista)
print(somar_lista(lista))
# soma =0
# for j in lista:
#     soma += j
# print(soma, somar_lista(lista))
    