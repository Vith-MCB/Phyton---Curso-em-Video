resultado = 0
y = 0
for x in range(1, 51):
    if x == 1:
        y += 1
        print(y)
    else:
        y += 2
        resultado += (y / x)
        print('{}/{} +'.format(y, x), end='')
print('\nResultado = {:.5f}'.format(resultado))
