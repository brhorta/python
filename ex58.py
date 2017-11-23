#EXERCICIO 58
from random import randint
computador = randint(0,10)
user = 11
palpites = 0
print('-='*20)
print('Tente adivinhar o número que pensei')
print('-='*20)
again = 'S'
while again == 'S':
    while computador != user:
        user = int(input('Digita um número: '))
        if user != computador:
            print('Ainda não! Tenta novamente')
        palpites += 1
    print('-=-'*4)
    print('Acertou! {}'.format(user))
    print('-=-'*4)
    print('Você tentou {} vezes até acertar.'.format(palpites))
    again = str(input('Quer jogar novamente? [S/N] ')).upper()
    if again == 'S':
        computador = randint(0,10)
        palpites = 0
    elif again !='N':
        print('Entendi...')
print('Ok, volte sempre!')
