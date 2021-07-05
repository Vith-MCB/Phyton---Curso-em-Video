import math
a = float(input('Indique o A: '))
b = float(input('Indique o B: '))
c = float(input('Indique o C: '))
delt = pow(b,2)-(4*a*c)

if delt < 0:
    print('A função não pode ser resolvida, pois o delta é negativo!')

print('Valor do delta: {}'.format(delt))
print('Raiz quadrada de Delta: {}'.format(math.floor(math.sqrt(delt))))
result = (-(b)+math.sqrt(delt))/(2*a)
result2 = (-(b)-math.sqrt(delt))/(2*a)
print('O resultado da expressão é:\nDelta positivo:{}\nDelta negativo: {}'.format(result,result2))