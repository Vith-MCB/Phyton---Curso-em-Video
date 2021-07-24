A = int(input('Informe um número: '))
B = int(input('Informe o segundo número: '))
if A > B:
    print('{} é maior que {}'.format(A,B))
elif A == B:
    print('{} é igual a {}'.format(A,B))
else:
    print('{} é menor que {}'.format(A,B))
