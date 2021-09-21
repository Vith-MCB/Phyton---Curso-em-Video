agenda = []
nomes = []
numnal = 0
while True:
    numnom = input().split()
    nom, num = numnom
    nomes.append(nom)
    t = [nom, num]
    agenda.append(t)
    print('(a) Adicionar telefones na agenda')
    print('(b) Procurar um telefone')
    print('(c) Parar o programa')
    perg = input()
    if perg == 'a':
        continue
    elif perg == 'b':
        pesqnom = str(input())
        if pesqnom in nomes:
            nummal = nomes.index(pesqnom)
            print(agenda[nummal])
        else:
            print('Não listado')
    elif perg == 'c':
        break
    print(agenda)
