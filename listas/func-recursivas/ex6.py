try:
    palavra = str(input('Digite uma palavra: '))
except:
    print('Tente novamente')
def inverter_palavra(palavra):
    if not palavra:
        return
    if len(palavra) == 1:
        return palavra
    return inverter_palavra(palavra[1:]) + palavra[0]
print(palavra)
print(inverter_palavra(palavra))