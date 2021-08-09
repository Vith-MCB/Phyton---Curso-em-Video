dep = float(input('Valor depositado: '))
tjur = float(input('Taxa de juros (Em %): '))
tempo = int(input('Tempo: '))
tjur /= 100
for x in range(1, tempo+1):
    mont = dep * pow(1+tjur, tempo)
    print('Montante {}º mes: {:.2f}'.format(x, mont))
