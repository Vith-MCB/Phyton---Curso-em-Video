dias = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantidade de Km percorridos: '))
pagar = (dias*60)+(km*0.15)
print('O valor a pagar é: {:.2f}'.format(pagar))