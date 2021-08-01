conti = 0
contpar = 0
for x in range(0, 5):
    y = int(input())
    if y % 2 == 0:
        contpar += 1
    else:
        conti += 1
print('Ímpares: {}\nPares: {}'.format(conti, contpar))
