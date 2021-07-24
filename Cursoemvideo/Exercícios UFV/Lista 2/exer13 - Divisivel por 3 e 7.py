num = int(input('Informe um número: '))
if num % 3 == 0 and num % 7 == 0:
    print('{} é divisível por 3 e 7!'.format(num))
else:
    print('{} não é divisível por 3 e 7!'.format(num))
