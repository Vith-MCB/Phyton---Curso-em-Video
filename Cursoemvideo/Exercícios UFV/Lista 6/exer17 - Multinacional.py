dados = []
vetor = []
while True:
    vetor.append(str(input('Nome do produto: ')))
    vetor.append(int(input('Valor do produto em dólar: US$ ')))
    dados.append(vetor[:])
    vetor.clear()
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar[N/S]: ')).upper()
    if resp == 'N':
        break
for n in range(len(dados)):
    print(f'O produto {dados[n][0]} custa US$ {dados[n][1]:.2f} ou R$ {dados[n][1] * 5.38:.2f}')
