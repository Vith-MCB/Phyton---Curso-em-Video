vet = [float(input()) for i in range(15)]
soma = 0
for i in range(15):
    soma += vet[i]
media = soma/len(vet)
print(f'Media dos alunos: {media}')
