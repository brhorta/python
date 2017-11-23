#EXERCÍCIO 59
num1 = 0
num2 = 0
op = 0
while op == 0:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o primeiro número: '))
    print('Você digitou {} e {}, escolha abaixo:'.format(num1, num2))
    op = int(input('[1]SOMAR \n[2]MULTIPLICAR \n[3]MAIOR \n[4]NOVOS NÚMEROS \n[5]SAIR DO PROGRAMA \n -> '))
    if op == 1:
        print('A soma de {} com {} é igual a {}'.format(num1, num2, (num1+num2)))
        op = 0
    elif op == 2:
        print('A multiplicação de {} com {} é igual a {}'.format(num1, num2, (num1 * num2)))
        op = 0
    elif op == 3:
        if num1 > num2:
            print('O maior número é {}.'.format(num1))
            op = 0
        elif num1 < num2:
            print('O maior número é {}.'.format(num2))
            op = 0
        else:
            print('Eles ão iguais.')
            op = 0
    elif op == 4:
        op = 0
    elif op == 5:
        print('Fim')
    elif op != 5 or op != 4 or op != 3 or op != 2 or op != 1:
        print('Vamos tentar novamente...')
        op = 0
