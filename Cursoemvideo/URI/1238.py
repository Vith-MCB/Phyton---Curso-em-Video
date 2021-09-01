n = int(input())
cont = 0
while cont < n:
    linha = input().split()
    palavra1 = linha[0]
    palavra2 = linha[1]
    palfin = ''
    cont2 = 0
    while cont2 < len(palavra1) and cont2 < len(palavra2):
        palfin += palavra1[cont2] + palavra2[cont2]
        cont2 += 1
    if cont2 < len(palavra1):
        palfin += palavra1[cont2:]

    if cont2 < len(palavra2):
        palfin += palavra2[cont2:]

    print(palfin)
    cont += 1
