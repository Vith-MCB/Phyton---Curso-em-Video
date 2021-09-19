N = int(input())
M = []
for i in range(N):
    x, y = [int(x) for x in input().split()]
    M.append([x, y])
areatotal = 0
for i in range(N):
    if i != 0:
        for j in range(i, -1, -1):
            if M[i][0] > M[j][0]:
                menorx = M[j][0]
            if M[i][1] > M[j][1]:
                menory = M[j][1]
        for j in range(i, -1, -1):
            try:
                if menorx < M[j][0] < M[i][0]:
                    menorx = M[j][0]
            except:
                if menory < M[j][1] < M[i][1]:
                    menory = M[j][1]
            try:
                if menory < M[j][1] < M[i][1]:
                    menory = M[j][1]
            except:
                if menorx < M[j][0] < M[i][0]:
                    menorx = M[j][0]
        areamenor = 0
        try:
            areamenor += menorx * M[i][1]
        except:
            sla = 0
        try:
            areamenor += menory * M[i][0]
        except:
            sla = 0
        areaquad = M[i][0] * M[i][1] - areamenor
    else:
        areaquad = M[i][0] * M[i][1]
    areatotal += areaquad
print(areatotal)