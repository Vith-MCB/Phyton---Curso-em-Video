peso = float(input('Peso em kg: '))
altura = float(input('Altura em m: '))
imc = peso//pow(altura, 2)
print(imc)
if imc < 20:
    print('Abaixo do peso')
elif imc in range(20, 25):
    print('Peso Normal')
elif imc in range(25, 30):
    print('Sobrepeso')
elif imc in range(30, 40):
    print('Obeso')
elif imc > 40:
    print('Obeso morbido')
