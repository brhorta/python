n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
md = (int(n1) + int(n2)) / 2
print(md)
print(type(md))
if md <= 5:
    print('Média abaixo de 5.0\nReprovado')
elif md > 5 and md < 6.9:
    print('Média entre de 5.0 e 6.9\nRecuperação')
elif md >= 7.0:
    print('Média {}\nAPROVADO!'.format(md))