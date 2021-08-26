peso_tot = valor_tot = 0
peso = []
valor = []
quant = int(input('Quantidade de caixas: '))
for n in range(quant):
    peso.append(float(input(f'Peso da {n + 1}ª caixa: ')))
    valor.append(float(input(f'Valor da {n + 1}ª caixa: ')))
    peso_tot += peso[n]
    valor_tot += valor[n]
valor_carga = float(input('Valor total dada carga: '))
print(f'O peso total da carga é: {peso_tot}')
print(f'O valor total das caixas é R$ {valor_tot:.2f}')
if valor_carga != valor_tot:
    print(f'Há conflito entre os valores.\nValor total da carga: R$ {valor_carga:.2f}')
else:
    print('Não há conflito entre os valores')