m = 8
if m <= 5:
    sit = 'Reprovado'
else:
    sit = 'Aprovado'
print('Você está: {}'.format(sit))
if m in range(6,8):
    print('Meus parabéns!')
elif m > 7:
    print('Que notão!!')