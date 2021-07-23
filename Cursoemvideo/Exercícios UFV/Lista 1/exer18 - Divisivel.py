A = int(input('Informe um número: '))
B = int(input('Informe um outro número: '))
if A%B == 0:
    print('{} é divisível por {}'.format(A,B))
else:
    print('{} não é divisível por {}'.format(A,B))