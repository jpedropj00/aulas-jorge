#SOMA DE 1 até N
while True:
    n = int(input('Digite o número: '))
    if n > 0:
        break
    else:
        print('Número inválido, tente novamente')
def soma(n):
    if n == 1:
        return 1
    return n + soma(n-1)    
print(soma(n))

