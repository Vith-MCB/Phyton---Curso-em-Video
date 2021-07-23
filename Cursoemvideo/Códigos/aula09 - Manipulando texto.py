frase = 'Curso em Video Python'
frase2 = '   Aprenda Python  '
print(frase[::2]) #Método de repartição da string (A partir de : Até : salto)
print('Espaços: {}'.format(len(frase))) #Quantidade de caracteres
print(frase.count('o')) #Quantidade de caracteres informados
print('Curso' in frase)
print(frase + ' //', frase.replace('Python','Android'))
print(frase.upper()) #p/ maiusc
print(frase.lower()) #p/ minusc
print(frase.capitalize()) #1º letra mantem, resto em minúsculo
print(frase.title()) #Primeiras letras em maiúsculas
print(frase2, '//', frase2.strip()) #remove espaços desnecessários
print(len(frase2))
print(len(frase2.strip()))
print(frase.split())
print('-'.join(frase.split()))



