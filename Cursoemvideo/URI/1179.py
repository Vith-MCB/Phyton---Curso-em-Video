par = []
impar = []
cont = 0
im = 0
p = 0
while cont < 15:
    num = int(input())
    if num % 2 == 0:
        par.append(num)
        p += 1
    else:
        impar.append(num)
        im += 1
    if p > 4:
        for i in range(5):
            print(f'par[{i}] = {par[i]}')
        par = []
        p = 0
    if im > 4:
        for y in range(5):
            print(f'impar[{y}] = {impar[y]}')
        impar = []
        im = 0
    cont += 1
if im > 0:
    for j in range(im):
        print('impar[{}] = {}'.format(j, impar[j]))
if p > 0:
    for h in range(p):
        print('par[{}] = {}'.format(h, par[h]))
