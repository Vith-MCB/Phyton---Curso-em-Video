import random
A = [[0 for i in range(3)] for j in range(4)]
B = [[0 for x in range(3)] for y in range(4)]
for i in range(3):
    for j in range(4):
        A[i][j] = random.randint(0, 1000)
for i in range(3):
    for j in range(4):
        B[i][j] = A[i][j] * 3
