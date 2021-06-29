preco = float(input('Informe o preço base do produto: '))
desc = int(input('De quanto será o desconto: '))
porc = desc/100
npreco = preco*(1-porc)
print('Com o desconto, o novo preço do produto será: {:.2f}'.format(npreco))