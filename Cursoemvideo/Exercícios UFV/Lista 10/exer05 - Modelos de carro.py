qtcar = int(input())
carkm = []
maior = 0
for i in range(qtcar):
    kmc = input().split()
    car, km = kmc
    t = [str(car), int(km)]
    carkm.append(t)
for j in range(qtcar):
    if maior < carkm[j][1]:
        maior = carkm[j][1]
        carrokm = carkm[j]
print(carrokm)
qtgas = (1000/maior) * 3.5
print(qtgas)
