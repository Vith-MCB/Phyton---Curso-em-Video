a = int(input('Comprimento reta a: '))
b = int(input('Comprimento reta b: '))
c = int(input('Comprimento reta c: '))
if a+b < c:
    print('Não é triangulo')
elif a+c < b:
    print('Não é triangulo')
elif b+c < a:
    print('Não é triangulo')
else:
    print('Podem formar um triângulo')
