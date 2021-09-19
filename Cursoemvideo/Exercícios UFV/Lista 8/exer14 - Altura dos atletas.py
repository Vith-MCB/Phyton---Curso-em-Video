import random
matriz = [[0 for i in range(10)] for j in range(5)]
maior = 0
for i in range(5):
    for j in range(10):
        matriz[i][j] = random.randint(100, 200)
        if matriz[i][j] > maior:
            maior = matriz[i][j]
    print(maior)
    maior = 0
