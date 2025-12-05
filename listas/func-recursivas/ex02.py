#Fatorial
while True:
    n=int(input('Digite um número: '))
    if n >= 0:
        break
    else:
        print('Número inválido')
def fatorial(n):
    if n == 0 or n == 1:
        return 1 
    return n * fatorial(n-1)
print(fatorial(n))
