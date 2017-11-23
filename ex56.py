menores = 0
maisvelho = 0
idade = 0
baseIdade = 0
for p in range(1, 5):
    print('-= Digite os dados da {}ª pessoa. =-'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maisvelho:
        maisvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        menores += 1
    if idade != 0:
        baseIdade += idade
mediaIdade = baseIdade / 4
print('A média de idade do grupo é {}'.format(mediaIdade))
print('O nome do homem mais velho é {} e tem {} anos.'.format(nomevelho,maisvelho).upper())
if menores != 0:
    print('Temos {} mulheres menores de 20 anos'.format(menores))
else:
    print('Não temos mulheres menores de 20 anos.')