import random
somadp = 0
matriz = [[0 for i in range(10)] for j in range(10)]
for i in range(10):
    for j in range(10):
        matriz[i][j] = random.randint(0, 1000)
n = 10
for i in range(10):
    n -= 1
    for j in range(1, n):
        print(matriz[i][j])
        somadp += matriz[i][j]
print(somadp)
print(matriz)
