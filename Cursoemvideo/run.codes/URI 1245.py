vett = []
vetp = []
contpares = 0
while True:
    try:
        n = int(input())
        for i in range(n):
            list1 = input().split()
            m, L = list1
            vett.append(int(m))
            vetp.append(L)
        for j in range(n-1):
            for y in range(n-1, 0, -1):
                if vett[j] == vett[y] and vetp[j] != vetp[y]:
                    contpares += 1
                if contpares == 2:
                    break
    except EOFError:
        break
    print(contpares)
