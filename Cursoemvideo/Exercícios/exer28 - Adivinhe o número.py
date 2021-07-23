import random
num = random.randint(0,5)
numus = int(input('Informe um inteiro (0 a 5): '))
if numus == num:
    print('Você venceu!')
else:
    print('O computador venceu!')