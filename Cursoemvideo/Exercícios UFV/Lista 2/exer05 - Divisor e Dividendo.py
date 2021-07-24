divid = float(input('Informe um número: '))
divis = float(input('Informe outro número: '))
if divis == 0:
    print('Divisão não permitida')
else:
    quo = divid/divis
    resto = divid%divis
    print('{} dividido por {} = {:.2f}'.format(divid,divis,quo))
    print('Resto = {:.0f}'.format(resto))