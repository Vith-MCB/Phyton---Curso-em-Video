A, B, C, D, E = 0, 0, 0, 0, 0
totidD = 0
maioridE, maioridA, maioridD = 0, 0, 0

for i in range(0, 5):
    idade = int(input('Idade: '))
    resposta = input('Nota: ')
    if resposta == 'A':
        A += 1
        if idade > maioridA:
            maioridA = idade
    if resposta == 'B':
        B += 1
    if resposta == 'C':
        C += 1
    if resposta == 'D':
        D += 1
        totidD += idade
        if idade > maioridD:
            maioridD = idade
    if resposta == 'E':
        E += 1
        if idade > maioridE:
            maioridE = idade
tot = A+B+C+D+E
percB = (B * 100)/tot
percC = (C * 100)/tot
percE = (E * 100)/tot
print('Quant. resp. A: {}'.format(A))
print('Dif. percent.: {}'.format(percB - percC))
print('Media idade RUIM: {}'.format(totidD/D))
print('Porc. pessimo: {} // Maior id: {}'.format(percE, maioridE))
print('Diferença: {}'.format(maioridA-maioridD))
