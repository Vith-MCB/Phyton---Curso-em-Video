import random
soma = 0
matriz = [[0 for i in range(4)] for j in range(5)]
for i in range(4):
    for j in range(5):
        matriz[i][j] = random.randint(0, 1000)
        soma += matriz[i][j]
