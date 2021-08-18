cont = int(input('De 0 a: '))
maior = 0
menor = 10000000
for i in range(0, cont):
    num = int(input())
    if num == -1:
        break
    elif num > maior:
        maior = num
    if num < menor:
        menor = num
print('Maior: {}\nMenor: {}'.format(maior, menor))
