m = 11
if m <= 5:
    sit = ('Reprovado')
else:
    sit = ('Aprovado')
print('Você está: {}'.format(sit))
if m in range(6,10):
    print('Meus parabéns!')
elif m > 10:
    print('Que notão!!')