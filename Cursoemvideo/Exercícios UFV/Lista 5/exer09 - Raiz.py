from math import sqrt
for i in range(0, 10):
    num = int(input())
    if num < 0:
        break
    print('Raiz quadrada: {:.2f}'.format(sqrt(num)))
