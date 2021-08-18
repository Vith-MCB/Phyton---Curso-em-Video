valcasa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
anos = float(input('Quantidade de anos: '))
prest = valcasa/(anos * 12)
if prest > sal * 1.3:
    print('Empréstimo negado!')
elif prest == sal * 1.3:
    print('Empréstimo aprovado NA TRAAAAVE!')
else:
    print('Emprestimo liberado!')
