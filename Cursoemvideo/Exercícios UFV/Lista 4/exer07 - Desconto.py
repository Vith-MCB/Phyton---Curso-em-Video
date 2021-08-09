preco = float(input('Preço original: '))
desc = preco * 0.09
preco *= 0.91
print('Valor do Desconto: R${:.2f}'.format(desc))
print('Novo preço: R${:.2f}'.format(preco))
