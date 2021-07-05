import math
c1 = float(input('Comprimento prim. cateto: '))
c2 = float(input('Comprimento seg. cateto: '))
hip = math.sqrt(c1**2+c2**2)
print('O comprimento da hipotenusa de um triângulo ret. com catetos {} e {} resulta: {}'.format(c1,c2,hip))