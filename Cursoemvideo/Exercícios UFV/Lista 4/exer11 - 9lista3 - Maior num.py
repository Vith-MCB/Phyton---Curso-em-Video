quant = int(input())
maior = 0
for x in range(1, quant+1):
    num = int(input())
    if num > maior:
        maior = num
print('Maior num.: {}'.format(maior))
