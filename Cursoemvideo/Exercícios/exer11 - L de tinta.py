h = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura: '))
tint = float(input('Quantidade de m. quadrados por litro da tinta: '))
print('Tamanho da parede em m^2: {}'.format(h*l))
qt = (h*l)/tint
print('Quntidade de tinta necessária: {:.1f}L'.format(qt))