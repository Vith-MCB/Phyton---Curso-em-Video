divis = 0
resultado = 0

x = int(input('Digite o valor de x: '))

for pot in reversed(range(1, 26)):
    divis += 1
    if pot % 2 == 0:
        print(' -', '{}^{}/{}'.format(x, pot, divis), end='')
        resultado -= x ** pot / divis
    else:
        print(' +', '{}^{}/{}'.format(x, pot, divis), end="")
        resultado += x ** pot / divis

print('\nResultado = {:.5f}'.format(resultado))