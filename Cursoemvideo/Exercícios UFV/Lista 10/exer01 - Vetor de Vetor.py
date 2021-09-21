import random
vetor = [0 for i in range(10)]
vetrepet = []
num, maior, repet = 0, 0, 0
for j in range(10):
    vetor[j] = random.randint(1, 10)
    if vetor[j] > maior:
        maior = vetor[j]
print(maior)
print(vetor)
for i in range(1, maior+1):
    if i in vetor:
        vetrepet.append(vetor.count(i))
    else:
        vetrepet.append(0)
print(vetrepet)
