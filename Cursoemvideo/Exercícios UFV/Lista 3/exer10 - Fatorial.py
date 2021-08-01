num = int(input("Digite o número: "))
if num > 0:
    fatorial = num
    for x in range(1, num):
        fatorial = fatorial * x
print('O fatorial de {} é {}'.format(num, fatorial))
