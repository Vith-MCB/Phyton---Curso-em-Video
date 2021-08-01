Soma = 0
Rm = 0
while True:
    w1, w2, r = [int(x) for x in input().split()]
    if w1 == w2 == r == 0:
        break
    M = float(((w1 * (1 + r/30))+(w2 * (1 + r/30))))/2.0
    Rm += M
    if 1 <= M < 13:
        print("Nao vai da nao")
    if 13 <= M <14:
        print("E 13")
    if 14 <= M < 40:
        print("Bora, hora do show! BIIR!")
    if 40 <= M < 60:
        print("Ta saindo da jaula o monstro!")
    if M > 60:
        print("AQUI E BODYBUILDER!!")
    Soma += 1
Rm = Rm /Soma
if Rm > 40:
    print()
    print("Aqui nois constroi fibra rapaz! Nao e agua com musculo!")