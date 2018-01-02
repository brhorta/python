print('='*30)
print('{:^30}'.format('BRUNO BANK'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
for cedula in (50, 20, 10, 1):
    print(f'Total de {valor // cedula} cédulas de R${cedula}')
    valor %= cedula
print('='*30)
print('Volte sempre ao BRUNO BANK! Tenha um bom dia!')