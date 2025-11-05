#LISTA 8 - Jorge
from math import pi
from random import randint
import numpy
def formatar_data():
  while True:
    while True:
      dia=int(input('Digite o dia: '))
      if dia < 1 or dia > 31:
        print('Dia inválido')
      else:
        break
    while True:
      mes=int(input('Digite o mês: '))
      if mes < 1 or mes > 12:
        print('Mês inválido')
      else:
        break
    while True:
      ano=int(input('Digite o ano: '))
      if ano < 0:
        print('Ano inválido')
      else:
        break
    break
  print(f"{dia:02d}/{mes:02d}/{ano:04d}")
def area_circulo():
  while True:
    raio=int(input('Digite o raio de um círculo: '))
    if raio < 0:
      print('Tente novamente, número inválido')
    else:
      break
  area= (raio ** 2) * pi
  print(f'A área do circulo de raio {raio:.2f} é igual a {area:.2f}')
def converter_para_celsius():
  fahrenheit=float(input('Digite a temperatura em fahrenheit: '))
  print('Convertendo...')
  C = (fahrenheit - 32) * (5 / 9)
  print(f'A temperatura {fahrenheit:.2f} em celsius fica {C:.2f}° C')
def calcular_hipotenusa():
  c1=float(input('Digite o tamanho do cateto 1: '))
  c2=float(input('DIgite o tamanho do cateto 2: '))
  hipotenusa= (c1 ** 2 + c2 ** 2) ** 0.5
  print(f"A hipotenusa do triângulo com catetos 1 {c1:.2f} e cateto 2 {c2:.2f} é igual a {hipotenusa:.2f}")
def calcular_bhaskara():
  while True:
    a = float(input('Coeficiente a: '))
    b = float(input('Coeficiente b: '))
    c = float(input('Coeficiente c: '))
    if a < 0 or b < 0 or c < 0:
      print('Algum número inválido! Tente novamente')
    else:
      break
  delta= b ** 2 - (4*a*c)
  if delta < 0:
    print('Não existe raiz real')
  else:
    if delta == 0:
      resp=(-b + (delta) ** 0.5) / (2 * a)
      print(f'Temos uma raiz real igual a {resp}')
    if delta > 0:
      resp1=(-b + (delta ** 0.5)) / (2 * a)
      resp2=(-b - (delta ** 0.5)) / (2 * a)
      print(f'Raiz 1: {resp1}\n Raiz 2: {resp2}')
def cont_letras():
  palavra=input('Digite a palavra: ')
  cont=0
  for i in palavra:
    cont+=1
  print(f'A palavra {palavra} tem {cont} letras.')
def palavra_contida():
  palavra1=input('Digite a primeira palavra: ')
  palavra2=input('Digite a segunda palavra: ')
  palavra1=palavra1.lower()
  palavra2=palavra2.lower()
  if palavra1 in palavra2:
    print('A primeira palavra está contida na segunda')
  else:
    print('Não está')
def gerar_vetor():
  tam=int(input('digite o tamanho do vetor: '))
  valorMin=int(input('digite o menor valor: '))
  valorMax=int(input('digite o maior valor da lista: '))
  lista=[randint(valorMin, valorMax) for _ in range(tam)]
  print('Vetor gerado...')
  print(f'Vetor gerado: {lista}')
  return lista
def maior_valor():
  escolha = int(input('''
  [1] Gerar Lista
  [2] Passar Lista
  '''))
  while True:
    if escolha < 0 or escolha > 2:
      print('Valor inválido')
    else:
      break
  if escolha == 1:
    lista=gerar_vetor()
  else:
    lista=[]
    tamLista=int(input('Digite o tamanho da lista: '))
    for i in range(tamLista):
      numLista=int(input('Digite o número para a lista: '))
      lista.append(numLista)
  maior=lista[0]
  cont=0
  for i in lista:
    cont+=1
  for j in range(cont):
    if lista[j] > maior:
      maior=lista[j]
  print(f'O maior valor da lista é {maior}')
def media_vetor():
  escolha = int(input('''
  [1] Gerar Lista
  [2] Passar Lista
  '''))
  while True:
    if escolha < 0 or escolha > 2:
      print('Valor inválido')
    else:
      break
  if escolha == 1:
    lista=gerar_vetor()
  else:
    lista=[]
    tamLista=int(input('Digite o tamanho da lista: '))
    for i in range(tamLista):
      numLista=int(input('Digite o número para a lista: '))
      lista.append(numLista)
  somaLista=0
  cont=0
  for i in lista:
    cont+=1
  for j in lista:
    somaLista+=j
  mediaLista=somaLista / cont
  print(f'A média da lista é igual a {mediaLista:.2f}')
def ordenar_vetor():
  while True:
    escolha = int(input('''
        [1] Gerar Lista
        [2] Passar Lista
        '''))
    if escolha < 0 or escolha > 2:
      print('Valor inválido')
    else:
      break
  if escolha == 1:
    lista=gerar_vetor()
  else:
    lista=[]
    tamLista=int(input('Digite o tamanho da lista: '))
    for i in range(tamLista):
      numLista=int(input('Digite o número para a lista: '))
      lista.append(numLista)
  cont=0
  for i in lista:
    cont+=1
  for i in range(cont-1):
    for j in range(i+1, cont):
      if lista[i] > lista[j]:
        lista[i], lista[j] = lista[j], lista[i]
  print(f'Lista ordenada: {lista}')
def ordenar_vetor_contrario():
    while True:
      escolha = int(input('''
        [1] Gerar Lista
        [2] Passar Lista
        '''))
      if escolha < 0 or escolha > 2:
        print('Valor inválido')
      else:
        break
    if escolha == 1:
      lista=gerar_vetor()
    else:
      lista=[]
      tamLista=int(input('Digite o tamanho da lista: '))
      for i in range(tamLista):
        numLista=int(input('Digite o número para a lista: '))
        lista.append(numLista)
    cont=0
    for i in lista:
      cont+=1
    for i in range(cont-1):
      for j in range(i+1, cont):
        if lista[i] < lista[j]:
          lista[i], lista[j] = lista[j], lista[i]
    print(f'Lista ordenada decrescente: {lista}')
def remove_rep():
    while True:
        escolha = int(input('''
[1] Gerar Lista
[2] Passar Lista
Escolha: '''))
        if escolha < 1 or escolha > 2:
            print('Valor inválido')
        else:
            break

    if escolha == 1:

        lista = gerar_vetor()
    else:
        lista = []
        tamLista = int(input('Digite o tamanho da lista: '))
        for _ in range(tamLista):
            numLista = int(input('Digite o número para a lista: '))
            lista.append(numLista)

    listaNorep = []
    for item in lista:
        if item not in listaNorep:
            listaNorep.append(item)

    print("Lista original:", lista)
    print("Lista sem repetições:", listaNorep)
    return listaNorep

def criar_matriz():
    numLinhas=int(input('Digite o número de linhas da matriz: '))
    numCol=int(input('Digite o número de colunas da matriz: '))
    limInf=int(input('Digite o menor valor da matriz: '))
    limSup=int(input('Digite o maior valor da matriz: '))
    matriz=[]
    for i in range(numLinhas):
        linha=[]
        for j in range(numCol):
            num=randint(limInf,limSup)
            linha.append(num)
        matriz.append(linha)
    print("Matriz gerada:")
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4}", end="")
        print()
    return matriz, numLinhas, numCol
def media_matriz():
   def media_matriz():
    while True:
        escolha = int(input('''
        [1] Gerar Matriz
        [2] Passar Matriz
        '''))
        if escolha < 0 or escolha > 2:
            print('Valor inválido')
        else:
            break
    if escolha == 1:
        matriz, numLinhas, numCol = criar_matriz()
    else:
        numLinhas=int(input('Digite o número de linhas da matriz: '))
        numCol=int(input('Digite o número de colunas da matriz: '))
        limInf=int(input('Digite o menor valor da matriz: '))
        limSup=int(input('Digite o maior valor da matriz: '))
        matriz=[]
        for i in range(numLinhas):
            linha=[]
            for j in range(numCol):
                num=randint(limInf,limSup)
                linha.append(num)
            matriz.append(linha)
    somaTotal = 0
    cont = 0
    for linha in matriz:
        for elemento in linha:
            somaTotal += elemento
            cont += 1
    media = somaTotal / cont
    print(f'A média dos valores da matriz é {media:.2f}')
def maior_valor_matriz():
 def maior_valor_matriz():
    while True:
        escolha = int(input('''
        [1] Gerar Matriz
        [2] Passar Matriz
        '''))
        if escolha < 0 or escolha > 2:
            print('Valor inválido')
        else:
            break
    if escolha == 1:
        matriz, numLinhas, numCol = criar_matriz()
    else:
        numLinhas=int(input('Digite o número de linhas da matriz: '))
        numCol=int(input('Digite o número de colunas da matriz: '))
        limInf=int(input('Digite o menor valor da matriz: '))
        limSup=int(input('Digite o maior valor da matriz: '))
        matriz=[]
        for i in range(numLinhas):
            linha=[]
            for j in range(numCol):
                num=randint(limInf,limSup)
                linha.append(num)
            matriz.append(linha)
    maior = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento > maior:
                maior = elemento
    print(f'O maior valor da matriz é {maior}')

def valor_acima_media():
   def valor_acima_media():
    while True:
        escolha = int(input('''
        [1] Gerar Matriz
        [2] Passar Matriz
        '''))
        if escolha < 0 or escolha > 2:
            print('Valor inválido')
        else:
            break
    if escolha == 1:
        matriz, numLinhas, numCol = criar_matriz()
    else:
        numLinhas=int(input('Digite o número de linhas da matriz: '))
        numCol=int(input('Digite o número de colunas da matriz: '))
        limInf=int(input('Digite o menor valor da matriz: '))
        limSup=int(input('Digite o maior valor da matriz: '))
        matriz=[]
        for i in range(numLinhas):
            linha=[]
            for j in range(numCol):
                num=randint(limInf,limSup)
                linha.append(num)
            matriz.append(linha)
    somaTotal = 0
    cont = 0
    for linha in matriz:
        for elemento in linha:
            somaTotal += elemento
            cont += 1
    media = somaTotal / cont
    listaAcimaMedia=[]
    for linha in matriz:
        for elemento in linha:
            if elemento >= media:
                listaAcimaMedia.append(elemento)
    print(f'Matriz: {matriz}')
    print(f'Os valores acima da média da matriz são: {listaAcimaMedia}')

def diagonal_matriz():
 def diagonal_matriz():
    while True:
        escolha = int(input('''
        [1] Gerar Matriz
        [2] Passar Matriz
        '''))
        if escolha < 0 or escolha > 2:
            print('Valor inválido')
        else:
            break
    if escolha == 1:
        matriz, numLinhas, numCol = criar_matriz()
    else:
        numLinhas=int(input('Digite o número de linhas da matriz: '))
        numCol=int(input('Digite o número de colunas da matriz: '))
        limInf=int(input('Digite o menor valor da matriz: '))
        limSup=int(input('Digite o maior valor da matriz: '))
        matriz=[]
        for i in range(numLinhas):
            linha=[]
            for j in range(numCol):
                num=randint(limInf,limSup)
                linha.append(num)
            matriz.append(linha)
    diag_principal=[]
    diag_secundaria=[]
    for i in range(min(numLinhas,numCol)):
        diag_principal.append(matriz[i][i])
        diag_secundaria.append(matriz[i][numCol-1-i])
    print(f'Diagonal principal: {diag_principal}')
    print(f'Diagonal secundaria: {diag_secundaria}')


print("MENU")
print('''
[0] Sair
[1] Exibir data
[2] Área da circunferência
[3] Converter Fahrenheit para Celsius
[4] Calcular hipotenusa
[5] Equação do 2º grau
[6] Contar letra em palavra
[7] Verificar palavra contida
[8] Gerar vetor aleatório
[9] Maior elemento do vetor
[10] Média do vetor
[11] Ordem crescente
[12] Ordem decrescente
[13] Remover repetições
[14] Gerar matriz aleatória
[15]Média da matriz
[16]Maior valor da matriz
[17]Valores acima e abaixo da média
[18]Diagonais da matriz
''')
while True:
  while True:
    escolha=int(input('Digite sua escolha: '))
    if escolha < 0 or escolha > 18:
      print('Número inválido')
    else:
      break
  if escolha == 0:
    print('Encerrando...')
    break
  elif escolha == 1:
    formatar_data()
  elif escolha == 2:
    area_circulo()
  elif escolha == 3:
    converter_para_celsius()
  elif escolha == 4:
    calcular_hipotenusa()
  elif escolha == 5:
    calcular_bhaskara()
  elif escolha == 6:
    cont_letras()
  elif escolha == 7:
    palavra_contida()
  elif escolha == 8:
    gerar_vetor()
  elif escolha == 9:
    maior_valor()
  elif escolha == 10:
    media_vetor()
  elif escolha == 11:
    ordenar_vetor()
  elif escolha == 12:
    ordenar_vetor_contrario()
  elif escolha == 13:
    remove_rep()
  elif escolha == 14:
    criar_matriz()
  elif escolha == 15:
    media_matriz()
  elif escolha == 16:
    maior_valor_matriz()
  elif escolha == 17:
    valor_acima_media()
  elif escolha == 18:
    diagonal_matriz()
