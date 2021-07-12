import random
p1 = input('Primeiro aluno: ')
p2 = input('Segundo aluno: ')
p3 = input('Terceiro aluno: ')
p4 = input('Quarto aluno: ')
list = [p1, p2, p3, p4]
esc = random.sample(list, 4)
print('A ordem de apresentação será: {}'.format(esc))