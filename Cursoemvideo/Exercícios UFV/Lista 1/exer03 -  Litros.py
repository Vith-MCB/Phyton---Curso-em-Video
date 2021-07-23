temp = int(input('Quanto tempo durou a viagem (horas)?'))
vm = float(input('Velocidade média: (Km/h): '))
dist = vm * temp
quantlit = dist/12
print('Dados da viagem: ')
print('Distância percorrida: {:2f} Km'.format(dist))
print('Quant. de combustível (l): {:.1f}'.format(quantlit))