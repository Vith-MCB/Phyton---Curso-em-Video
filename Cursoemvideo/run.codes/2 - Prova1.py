t1 = 2
t2 = 3
cont = 1
id = int(input())
while t1 < id:
   t3 = t1 + t2
   t1 = t2
   t2 = t3
   cont += 1
if cont % 2 == 0:
   print('pato')
elif cont % 2 == 1:
   print('ganso')
