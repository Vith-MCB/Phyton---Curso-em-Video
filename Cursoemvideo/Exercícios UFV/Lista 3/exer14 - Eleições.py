from random import randint
vcand1, vcand2, vcand3, vcand4 = 0, 0, 0, 0
vnulo, vbranco = 0, 0
for i in range(0,1000):
    voto = randint(1,6)
    if voto == 1:
        vcand1 += 1
    if voto == 2:
        vcand2 += 1
    if voto == 3:
        vcand3 += 1
    if voto == 4:
        vcand4 += 1
    if voto == 5:
        vnulo += 1
    if voto == 6:
        vbranco += 1
    totvotoscand = vcand1+vcand2+vcand3+vcand4
    percent = (vnulo+vbranco)/(totvotoscand+vnulo+vbranco)
print('Votos Cand. 1: {}\nVotos Cand. 2: {}'.format(vcand1, vcand2))
print('Votos Cand. 3: {}\nVotos Cand. 4: {}'.format(vcand3, vcand4))
print('Votos Nulos: {}\nVotos em Branco: {}'.format(vnulo, vbranco))
print('Percentural Nulos e Brancos: {:.1f}%'.format(percent*100))
