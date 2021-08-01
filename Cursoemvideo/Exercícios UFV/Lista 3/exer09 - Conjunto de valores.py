quantnum = 0
total = 0
while True:
    num = int(input('Digite um número: '))
    if num == -1:
        break
    if num >= 0:
        quantnum += 1
        total += num
        media = total/quantnum
print('Média: {}'.format(media))
