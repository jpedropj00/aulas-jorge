def simularTiro(linhaInicial, colInicial, direcao, tabuleiro):
    cima = (
        -1, 0
    )
    baixo = (
        1,0
    )
    esquerda = (
        0,1
    )
    direita = (
        1,0
    )
        
while True:
    numLinha = int(input('Digite o o número de linhas:'))
    numCol = int(input('Digite o número de colunas: '))
    if numLinha <= 1 or numCol <= 1:
        print('Número inválido! Tente novamente.')
    else:
        break
tabuleiro = []
for i in range(numLinha):
    linha = []
    for j in range(numCol):
        linha.append('.')
    tabuleiro.append(linha)
print(tabuleiro)