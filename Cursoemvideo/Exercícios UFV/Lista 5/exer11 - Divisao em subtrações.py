A = int(input('Digite um número: '))
B = int(input('Digite outro número: '))
neg = 0
if A < 0:
    neg = A
    A *= - 1
resto = A
while resto >= B:
    resto -= B
if neg < 0:
    resto *= - 1
print(f'O resto da divisão entre {A}/{B} é {resto}')
