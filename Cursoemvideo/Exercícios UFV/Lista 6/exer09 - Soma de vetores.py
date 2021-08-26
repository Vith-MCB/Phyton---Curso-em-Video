vet1 = [int(input()) for i in range(5)]
vet2 = [int(input()) for y in range(5)]
soma = 0
cont = 1
for x in range(5):
    soma = vet1[x] + vet2[x]
    print(f'soma {cont}º pos: {soma}')
    cont += 1
