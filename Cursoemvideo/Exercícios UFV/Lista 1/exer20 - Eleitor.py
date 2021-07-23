idade = int(input('Qual a idade do eleitor: '))
if idade < 16:
    print('Não Eleitor')
elif idade in range(18, 65):
    print('Eleitor obrigatório')
elif idade in range(16, 18) or idade > 65:
    print('Eleitor Facultativo')
