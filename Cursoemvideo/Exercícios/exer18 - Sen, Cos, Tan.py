import math
ang = float(input('Informe um ângulo: '))
angrad = math.radians(ang)
sen = math.sin(angrad)
cos = math.cos(angrad)
tg = math.tan(angrad)
print('Sen: {:.2f}\nCos: {:.2f}\nTang: {:.2f}'.format(sen,cos,tg))
