vet = []
soma = 0
Len = int(input('Tamanho do vetor: '))
for i in range(Len):
    vet.append(int(input()))
for i in range(Len):
    if vet[i] % 2 == 0:
        soma += vet[i]
print(f'Soma dos valores pares: {soma}')
