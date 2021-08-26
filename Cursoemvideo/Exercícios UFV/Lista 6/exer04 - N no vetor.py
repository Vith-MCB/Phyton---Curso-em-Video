vet = [int(input()) for i in range(5)]
n = int(input())
if n in vet:
    print(f'O numero {n} está na posição {vet.index(n)+1}')
else:
    print('Erro!')
