import random
matriz = [[0 for i in range(10)] for y in range(10)]
for i in range(10):
    for y in range(10):
        matriz[i][y] = random.randint(10, 99)
for i in range(10):
    print(matriz[i][i])
print(matriz)
