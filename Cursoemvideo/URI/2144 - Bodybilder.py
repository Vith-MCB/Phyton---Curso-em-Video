m = 0
loops = 0
i = int(1)
while i != 0:
    inputs = str(input())
    inp = inp.split()
    W1 = int(inp[0])
    W2 = int(inp[1])
    R = int(inp[2])
    Rm = float(((W1 * (1 + R / 30)) + (W2 * (1 + R / 30))) / 2.00)
    if 1 <= Rm < 13:
        print('Nao vai da nao')
    elif 13 <= Rm < 14:
        print('E 13')
    elif 14 <= Rm < 40:
        print('Bora, hora do show! BIIR!')
    elif 40 <= Rm <= 60:
        print('Ta saindo da jaula o monstro!')
    elif Rm > 60:
        print('AQUI E BODYBUILDER!!')
    m += Rm
    loops += 1
    if W1 == 0 and W2 == 0 and R == 0:
        i = 0
media = m / loops
if media > 40:
    print('')
    print('Aqui nois constroi fibra rapaz! Nao e agua com musculo!')