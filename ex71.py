print('='*31)
print('          BRUNO BANK          ')
print('='*31)
cinquenta = 50
vinte = 20
dez = 10
um = 0.0
total = 0
valor = int(input('Que valor você quer sacar? R$'))
dc = valor / cinquenta
sobrac = valor - (int(dc)*50)
dv = sobrac / vinte
sobrav = sobrac - (int(dv)*20)
dd = sobrav / dez
sobrad = sobrav - (int(dd)*10)
if sobrad >= 1:
    um = sobrad
#ABAIXO TESTES PARA VERIFICAR OS VALORES DE SAÍDA
'''print(f'dividido por 50 = {int(dc)}')
print(f'sobram = {sobrac}')
print(f'dividido por 20 = {int(dv)}')
print(f'sobram = {sobrav}')
print(f'dividido por 10 = {int(dd)}')
print(f'sobram = {sobrad}')
print(dc, dv, dd, um)'''
print('-'*31)
if int(dc) != 0:
    print(f'Total de {int(dc)} cédulas de R$50')
if int(dv) != 0:
    print(f'Total de {int(dv)} cédulas de R$20')
if int(dd) != 0:
    print(f'Total de {int(dv)} cédulas de R$10')
if um != 0:
    print(f'Total de {int(um)} cédulas de R$1')
print('='*31)
print('Volte sempre ao BRUNO BANK! Tenha um bom dia!')