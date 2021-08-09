a1 = int(input('Primeiro termo: '))
n = int(input('Numero do termo: '))
razao = int(input('Razão da P.G.: '))
an = pow(razao, n-1) * a1
print('Numero: {}'.format(an))
