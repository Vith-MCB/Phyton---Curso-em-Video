n = int(input())
for a in range(0, n):
    numero = input()
    mE = int(numero.split()[0])
    mD = int(numero.split()[1])
    if mE == mD and mE == 1:
        print('coma')
    else:
        print('pense')
