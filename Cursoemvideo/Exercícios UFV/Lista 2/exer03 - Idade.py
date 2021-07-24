anos = int(input('Idade (anos): '))
meses = int(input('Idade (meses): '))
dias = int(input('Idade (dias): '))
totdias = (anos*365)+(meses*30)+dias
print('Idade apenas em dias: {}'.format(totdias))
