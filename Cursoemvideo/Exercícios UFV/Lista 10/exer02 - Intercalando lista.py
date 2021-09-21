import random
l1 = []
l2 = []
resto = []
taml1 = random.randint(1, 5)
taml2 = random.randint(5, 10)
for i in range(taml1):
    l1.append(random.randint(1, 10))
for j in range(taml2):
    l2.append((random.randint(10, 100)))
for y in range(taml1, taml2):
    resto.append(l2[y])
lintercalada = [*sum(zip(l1, l2), ())] + resto
print(l1)
print(l2)
print(lintercalada)
