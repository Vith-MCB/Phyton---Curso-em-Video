nome = input('Qual o nome do funcionário? ')
sal = float(input('Informe o salário base: '))
aum = int(input('Informe a porcentagem de aumento: '))
porc = aum/100
nsal = sal*(1+porc)
print('O novo salário do funcionário {}, será: {:.2f}'.format(nome,nsal))
