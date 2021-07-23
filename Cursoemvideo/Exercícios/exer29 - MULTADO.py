vel = float(input('Informe a velociadade do carro (Km/h):  '))
if vel > 80:
    print('Você foi multado.')
else:
    print('Você não recebeu uma multa.')
kmlim = vel - 80
if kmlim > 0:
    print('Valor da multa: {:.2f}'.format(kmlim*7))
else:
    print('Não há multa a pagar!')