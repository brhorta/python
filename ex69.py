maior = 0
masc = 0
mulherMenor = 0
while True:
    print('-' * 28)
    print('    CADASTRE UMA PESSOA')
    print('-' * 28)
    continua = 'w'
    sexo = 'z'
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper()
    print('-'*28)
    while continua not in 'SN':
        continua = str(input('Quer continuar: [S/N]')).upper()
#    print('-' * 28)
    if sexo == 'M':
        masc += 1
    if idade >= 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        mulherMenor += 1
    if continua == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
print(f'Total de pessoas com mais de 18 anos: {maior}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {mulherMenor} mulheres com menos de 20 anos')