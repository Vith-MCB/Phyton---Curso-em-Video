maior = 0
for i in range(0, 16):
    num = int(input())
    if num > 30:
        maior += 1
print('\nMaiores que 30: {}'.format(maior))
