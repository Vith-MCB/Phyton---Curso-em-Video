pesoterr = int(input('Informe o peso na terra: '))
print('1- Mercúrio//2- Vênus//3- Marte//4- Jupiter//5- Saturno//6- Urano')
plan = int(input('Informe o planeta: '))
if plan == 1:
    peso = pesoterr * 0.37
    print('Peso em Mercúrio: {}'.format(peso))
if plan == 2:
    peso = pesoterr * 0.88
    print('Peso em Vênus: {}'.format(peso))
if plan == 3:
    peso = pesoterr * 0.38
    print('Peso em Marte: {}'.format(peso))
if plan == 4:
    peso = pesoterr * 2.64
    print('Peso em Jupiter: {}'.format(peso))
if plan == 5:
    peso = pesoterr * 1.15
    print('Peso em Saturno: {}'.format(peso))
if plan == 6:
    peso = pesoterr * 1.17
    print('Peso em Urano: {}'.format(peso))
