vetor1 = []
vetor2 = []
vetor3 = []
resp = 0
while True:
    vetor1.append(int(input('Digite um número: ')))
    vetor2.append(int(input('Digite outro número: ')))
    resp = ' '
    while resp not in 'NS':
        resp = str(input('Quer continuar[N/S]: ')).upper()
    if resp == 'N':
        break
for n in range(len(vetor1)):
    vetor3.append(vetor1[n])
    vetor3.append(vetor2[n])
print(vetor1)
print(vetor2)
print(vetor3)