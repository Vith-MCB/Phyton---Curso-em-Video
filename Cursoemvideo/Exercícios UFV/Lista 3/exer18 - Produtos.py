divisor = 0
resultado = 0
for x in reversed(range(2, 39)):
    divisor += 1
    resultado += ((x - 1) + x) / divisor
    print('{}*{}/{}'.format(x-1, x, divisor))
print('Resultado = '.format(resultado))

