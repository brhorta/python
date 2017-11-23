valor = float(input('Digite o valor do produto: '))
dinChq = valor * 0.9
aVista = valor * 0.95
ate2x = valor
tresOuMais = valor * 1.2

forma = int(input('Qual será a forma de pagamento? Escolha abaixo:''\n[ 1 ] À VISTA(dinheiro ou cheque)\n'
                  '[ 2 ] À VISTA(no cartão)\n[ 3 ] EM ATÉ 2X(no cartão)\n[ 4 ] EM 3X(ou mais)\n'))
if forma == 1:
    print('O valor será R$ {}'.format(dinChq))
elif forma == 2:
    print('O valor será R$ {}'.format(aVista))
elif forma == 3:
    print('O valor será 2 x de R$ {}'.format(ate2x / 2))
else:
    vezes = int(input('Quantas vezes? (3 ou mais)'))
    print('O valor será {} de R$ {:.2f}'.format(vezes, float(tresOuMais) / vezes))