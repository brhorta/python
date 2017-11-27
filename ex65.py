print('-='*20)
print('Digite 4 valores para obter sua média')
print('-='*20)
sair = 'N'
cont = 0
soma = 0
maior = 0
menor = 0
while sair == 'N':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        menor = num
        maior = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    elif cont == 4:
        print('-=' * 16)
        sair = str(input('Deseja sair?[S/N]')).upper()
        print('-=' * 16)
media = soma / cont
print('A média entre os valores foi de {}\n e o maior valor foi {} e o menor {}'.format(media, maior, menor))
print('fim')