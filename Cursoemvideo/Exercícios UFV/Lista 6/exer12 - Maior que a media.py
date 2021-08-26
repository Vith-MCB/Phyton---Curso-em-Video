altura = [float(input()) for i in range(10)]
som = 0
for i in range(10):
    som += altura[i]
media = som/len(altura)
for i in range(10):
    if altura[i] > media:
        print(altura[i])
