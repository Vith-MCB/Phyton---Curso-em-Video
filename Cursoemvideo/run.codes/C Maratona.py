N = int(input())
contm, contn, conta, contr, contt, conto = 0, 0, 0, 0, 0, 0
maratona = ['M', 'A', 'R', 'T', 'O', 'N']
palavra = input()

def fat(n):
    x = n
    for i in range(n-1, 1, -1):
        x *= i
    return x

if 'M' in palavra:
    contm = palavra.count('M')
if 'A' in palavra:
    conta = palavra.count('A')
if 'R' in palavra:
    contr = palavra.count('R')
if 'T' in palavra:
    contt = palavra.count('T')
if 'O' in palavra:
    conto = palavra.count('O')
if 'N' in palavra:
    contn = palavra.count('N')

anagramas = fat(len(palavra))/(fat(conta) * fat(contr) * fat(contt) * fat(conto) * fat(contn) * fat(contm))
print(anagramas)
