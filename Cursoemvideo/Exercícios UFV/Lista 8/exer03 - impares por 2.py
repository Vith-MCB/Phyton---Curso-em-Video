matriz = [[0 for i in range(7)] for y in range(5)]
for i in range(7):
    for j in range(5):
        matriz[i][j] = int(input())
        if matriz[i][j] % 2 != 0:
            matriz[i][j] *= 2
for i in range(7):
    for j in range(5):
        print(matriz[i][j])
