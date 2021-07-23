dis = float(input('Distância (Km/h): '))
if dis <= 200:
    print('O preço da passagem será: R$ {:.2f}'.format(dis*0.5))
else:
    print('O preço da passagem será: R$ {:.2f}'.format(dis*0.45))
