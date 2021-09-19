import random
A = [[0 for i in range(4)] for j in range(4)]
B = [[0 for x in range(4)] for y in range(4)]
for i in range(4):
    for j in range(4):
        A[i][j] = random.randint(0, 1000)
        B[i][j] = random.randint(0, 1000)
        print(A[i][j] - B[i][j])
