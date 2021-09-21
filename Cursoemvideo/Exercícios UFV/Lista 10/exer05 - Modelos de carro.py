qtcar = int(input())
carkm = []
maior = 0
for i in range(qtcar):
    kmc = input().split()
    car, km = kmc
    t = [str(car), int(km)]
    carkm.append(t)
print(carkm)
for j in range(qtcar):
    if maior < carkm[j][1]:
        maior = carkm[j][1]
print(maior)
