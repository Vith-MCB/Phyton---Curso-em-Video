h = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura: '))
print('Tamanho da parede em m^2: {}'.format(h*l))
qt = (h*l)/2
print('Quntidade de tinta necessária: {:.1f}L'.format(qt))