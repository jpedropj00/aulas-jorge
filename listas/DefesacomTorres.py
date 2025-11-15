def add_tabuleiro(tabuleiro, numLinha, numCol):
    numInimigos = int(input('Digite o número de inimigos: '))
    numTorres = int(input('Digite o número de torres: '))
    for i in range(numInimigos):
        while True:
            linhaInimigo = int(input(f'Digite a linha: '))
            colInimigo = int(input('Digite a coluna: '))
            if linhaInimigo < 0 or linhaInimigo >= numLinha or colInimigo < 0 or colInimigo >= numCol:
                print('Posição invalida, tente novamente')
            if tabuleiro[linhaInimigo][colInimigo] != '.':
                print('Posição já ocupada, tente novamente')
            else:
                tabuleiro[linhaInimigo][colInimigo] = 'n'
                break
    for j in range

                
                
                
    
def simularTiro(linhaInicial, colInicial, direcao, tabuleiro, numLinha, numCol):
    contAtaque = 0
    contTorresDestruidas = 0
    cima = (
        -1, 0
    )
    baixo = (
        1,0
    )
    esquerda = (
        0,-1
    )
    direita = (
        0,1
    )
    if direcao == 1:
        direcao = cima
    elif direcao == 2:
        direcao = baixo
    elif direcao == 3:
        direcao = esquerda
    elif direcao == 4:
        direcao = direita
        
    
        
    linhaAtual = linhaInicial + direcao[0]
    colAtual = colInicial + direcao[1]
    while 0 <= linhaAtual < numLinha and 0 <= colAtual < numCol:
        localization = tabuleiro[linhaAtual][colAtual]
        if localization == '.':
            pass
        elif localization == 'n':
            contAtaque += 1
            tabuleiro[linhaAtual][colAtual] = 'x'
            break
        elif localization == 't':
            contTorresDestruidas += 1
            print('Torre destruida')
            tabuleiro[linhaAtual][colAtual] = '.'
            break
        elif localization == '#':
            print('Tiro bloqueado')
            break
        linhaAtual += direcao[0]
        colAtual += direcao[1]
        
        
    return {
        'ataques': contAtaque,
        'torres_destruidas': contTorresDestruidas
    }
        
            
            
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