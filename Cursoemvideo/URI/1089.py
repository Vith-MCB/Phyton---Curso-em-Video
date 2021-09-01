
while True:
    picos = 0
    n = int(input())
    if n == 0:
        break
    h = [int(x) for x in input().split()]
    h.append(h[0])
    h.append(h[1])
    for y in range(1, n+1):
        if h[y] < h[y-1] and h[y] < h[y+1]:
            picos += 1
        elif h[y] > h[y-1] and h[y] > h[y+1]:
            picos += 1
    print(picos)
