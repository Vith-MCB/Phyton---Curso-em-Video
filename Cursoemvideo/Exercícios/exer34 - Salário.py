salario = float(input('Digite o salário do funcionário: '))
aum = salario
if salario > 1250:
    aum *= 0.1
    salario += aum
else:
    aum *= 0.15
    salario += aum
print('O novo salário será de: {}'.format(salario))
