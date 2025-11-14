while True:
    r = int(input('Digite o o número de linhas:'))
    s = int(input('Digite o número de colunas: '))
    numLadrao=int(input('Digite o número de ladrões: '))
    if r <= 1 or s <= 1 or numLadrao < 1:
        print('Número inválido! Tente novamente.')
    else:
        break
matriz = []
valor = ['.', 'T', 'n']
for i in range(r):
    linha = []
    for j in range(s):
        linha.append(0)
    matriz.append(linha)
    