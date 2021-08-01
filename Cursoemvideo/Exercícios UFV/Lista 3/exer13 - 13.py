totprodimp = 1
contpar = 0
while True:
    num = int(input())
    if num <= 0:
        break

    if num % 2 == 0:
        contpar += num
    else:
        totprodimp *= num
print('Soma dos pares: {}\nProduto dos ímpares: {}'.format(contpar,totprodimp))

