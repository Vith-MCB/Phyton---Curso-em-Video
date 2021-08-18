testes = int(input())
for i in range(0, testes):
    num = input()
    E = int(num.split()[0])
    D = int(num.split()[1])
    if E == D and E == 1:
        print('coma')
    else:
        print('pense')
