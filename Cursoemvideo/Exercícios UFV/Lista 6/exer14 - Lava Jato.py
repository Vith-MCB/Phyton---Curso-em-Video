idveic = []
valor = []
cont, soma = 0, 0
while True:
    idveic.append(int(input('Id do cliente: ')))
    if idveic[cont] < 0:
        break
    valor.append(float(input('Valora pagar: ')))
    soma += valor[cont]
    cont += 1
print(f'Total caixa: {soma}')
