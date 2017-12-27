from random import randint

print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=' * 15)
qual = 'o'
ganhou = 0
resultado = 'PAR'
while True:
    comp = randint(1, 4)
    valor = int(input('Digite um valor: '))
    qual = str(input('Par ou Ímpar? [P/I]')).upper()
    while qual not in 'PpIi':
        qual = str(input('Par ou Ímpar? [P/I]')).upper()
    if qual == 'P':
        qual = 'PAR'
    else:
        qual = 'ÍMPAR'
    soma = valor + comp
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print('-' * 30)
    print(f'Você jogou {valor} e o computador {comp}. Total de {soma}. DEU {resultado} e vc escolheu {qual}')
    if resultado == qual:
        print('VOCÊ VENCEU!')
        print('Vamos jogar novamente...')
        ganhou += 1
    else:
        print('VOCÊ PERDEU!')
        es = 'es'
        if ganhou == 0:
            es = ''
            ganhou = 'nenhuma'
        print(f'GAME OVER! Você venceu {ganhou} vez{es}.')
        break
