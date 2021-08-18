mult = 0
mult3 = 0
quant = int(input('Quantos numero você quer citar: '))
for i in range(0, quant):
    num = int(input())
    if num % 3 == 0:
        mult += 1
        mult3 += num
    if num < 0:
        break
media = mult3 / mult
print('Media: {}'.format(media))
