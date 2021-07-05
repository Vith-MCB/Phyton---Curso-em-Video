import math
numero = float(input('Digite um número real: '))
if (math.floor(numero)-numero <= -0.5):
    print('Numero em inteiro: {}'.format(math.ceil(numero)))
else:
    print('Numero em inteiro: {}'.format(math.floor(numero)))

