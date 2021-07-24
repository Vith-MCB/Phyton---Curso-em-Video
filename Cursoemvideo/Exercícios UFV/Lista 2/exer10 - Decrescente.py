A = int(input('Informe o 1º número: '))
B = int(input('Informe o 2º número: '))
C = int(input('Informe o 3º número: '))
if C > B:
    guardavalor = C
    C = B
    B = guardavalor
if B > A:
    guardavalor = B
    B = A
    A = guardavalor
if C > B:
    guardavalor = C
    C = B
    B = guardavalor
print(A,B,C)
