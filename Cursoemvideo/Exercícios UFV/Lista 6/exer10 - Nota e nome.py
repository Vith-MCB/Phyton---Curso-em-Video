nota = []
nome = []
maior, alma, alme, menor = 0, 0, 0, 999999999
for i in range(5):
    nome.append(input('Nome: '))
    nota.append(int(input('Nota: ')))
for y in range(5):
    if nota[y] > maior:
        alma = y
        maior = nota[y]
    if menor > nota[y]:
        alme = y
        menor = nota[y]
print(f'Maior nota: {maior} Aluno: {nome[alma]}')
print(f'Menor nota: {menor} Aluno: {nome[alme]}')
