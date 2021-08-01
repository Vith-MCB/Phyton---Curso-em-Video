from random import randint
sim, nao, femsim, mascnao = 0, 0, 0, 0
for i in range (0, 2000):
    voto = randint(1, 2)
    sexo = randint(1, 2)
    if voto == 1:
        sim += 1
    if voto == 2:
        nao += 1
    if voto == 1 and sexo == 2:
        mascnao += 1
    if voto == 2 and sexo == 1:
        femsim += 1
print('Votos SIM: {}\nVotos NÃO: {}'.format(sim, nao))
print('Fem. SIM: {}\nMasc. NÃO: {}'.format(femsim, mascnao))