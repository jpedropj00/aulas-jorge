# lista = [1,1]
# while True:
#     numEscolhido = int(input('Digite uma posição: '))
#     if numEscolhido >=1:
#         break
# def fibonacci(lista,numEscolhido):
#     if numEscolhido == 1 or numEscolhido == 2:
#         return 1
#     lista.append(lista[-1] + lista[-2])
#     if numEscolhido != len(lista):
#         fibonacci(lista,numEscolhido)
#     return lista[numEscolhido-1]
# print(fibonacci(lista,numEscolhido))
def fib(n):
    if n <= 0:
        raise ValueError("Posição deve ser >= 1")
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("Digite a posição desejada: "))
print(fib(n))

