print('-'*28)
print('     LOJA SUPER BARATÃO     ')
print('-'*28)
cont = 0
total = 0
preco = 0
maisdemil = 0
nomebarato = 'w'
precobarato = 0
while True:
    continua = 'w'
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    if cont == 0:
        precobarato = preco
        cont +=1
    if preco != 0 and preco < precobarato:
        precobarato = preco
        nomebarato = nome
    if preco > 1000:
        maisdemil += 1
    total += preco
    while continua not in 'SN':
        continua = str(input('Quer continuar: [S/N]')).upper()
    if continua == 'N':
        print('====== FIM DO PROGRAMA ======')
        break
print(f'O total da compra foi R${total}')
print(f'Temos {maisdemil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomebarato} que custa R${precobarato}')