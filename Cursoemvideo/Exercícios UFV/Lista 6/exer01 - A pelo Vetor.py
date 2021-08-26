vet = []
a = int(input('Valor de a: '))
for i in range(30):
    vet.append(int(input()))
for i in range(30):
    prod = a*vet[i]
    print(f'{a} * {vet[i]} = {prod}')
