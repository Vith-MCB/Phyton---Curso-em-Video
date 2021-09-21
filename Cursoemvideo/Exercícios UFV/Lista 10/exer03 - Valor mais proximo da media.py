import random
notas = []
soma, posi = 0, float(0)
menor = 100
quantn = random.randint(2, 10)
for i in range(quantn):
    notas.append(random.randint(0, 10))
    soma += notas[i]
media = soma/quantn
print(notas)
print(media)
for j in range(quantn):
    dif = notas[j] - media
    if dif < 0:
        posi = dif * (-1)
    else:
        posi = dif

    if menor > posi:
        menor = posi
if dif > 0:
    print(int(media + menor))
else:
    print(int(media - menor))
