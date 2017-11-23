from math import pow
altura = float(input('Digite sua altura '))
peso = float(input('Digite seu peso '))
imc = peso / (altura * altura)
print('Seu índice de massa corpórea é {:.2f}.'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso ideal')
elif imc >= 25.1 and imc <= 30:
    print('Sobrepeso')
else:
    print('Obesidade mórbida')