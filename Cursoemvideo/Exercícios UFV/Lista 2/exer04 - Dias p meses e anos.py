idade = int(input('Idade em dias: '))
anos = (idade//365)
meses = (idade - (anos * 365))//30
dias = idade - ((anos * 365)+(meses * 30))
print('Idade: \nAnos: {}\nMeses: {}\nDias: {}'.format(anos,meses,dias))
