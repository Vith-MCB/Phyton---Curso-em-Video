cav = int(input())
for i in range(cav):
    mons = int(input())
    vida = [[0 for x in range(cav)] for j in range(mons)]
    for j in range(mons):
        vida[i][j] = int(input())
        print(vida)
