'''
num = int(input('Informe um número de 1 a 7: '))
if num > 7 or num <= 0:
    print('Dia da semana inválido!')
else:
    lista = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado']
    if lista[num-1] == 'Domingo' or lista[num-1] == 'Sabado':
        print(lista[num-1])
    else:
        print('{}-Feira'.format(lista[num - 1]))
'''
num = int(input('Informe um número de 1 a 7: '))
if num > 7 or num <= 0:
    print('Dia da semana inválido!')
if num == 1:
    print('Domigo')
if num == 2:
    print('Segunda-Feira')
if num == 3:
    print('Terça-Feira')
if num == 4:
    print('Quarta-Feira')
if num == 5:
    print('Quinta-Feira')
if num == 6:
    print('Sexta-Feira')
if num == 7:
    print('Sábado')
