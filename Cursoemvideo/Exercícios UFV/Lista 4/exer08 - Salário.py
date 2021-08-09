aulasmes = int(input('Aulas por mês: '))
horas = int(input('Horas por aula: '))
horaaula = int(input('Valor da hora/aula : '))
inss = int(input('Desconto INSS (Em %): '))
inss /= 100
saliq = horas*aulasmes*horaaula
salbrut = saliq - (saliq * inss)
print('Salário Liquido: R${:.2f}'.format(saliq))
print('Salário Bruto: R${:.2f}'.format(salbrut))
