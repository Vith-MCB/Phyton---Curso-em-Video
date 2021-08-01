sal = float(input('Informe o salário: '))
prest = float(input('Valor da prestação: '))
if ((prest*100)/sal) > 30:
    print('O emprestimo não pode ser concedido.')
else:
    print('O empréstimo pode ser concedido!')
