from random import randint

mao = int(input('Vamos jogar pedra papel e tezoura?\n'
                '[1] PEDRA\n[2] PAPEL\n[3] TEZOURA\nEscolha sua mão: '))

comp = randint(1,3)
print('Pensei em {}'.format(comp))

if mao == comp:
    print('Empatou')
elif mao == 1 and comp == 2:
    print('Você perdeu')
elif mao == 1 and comp == 3:
    print('Você ganhou')
elif mao == 2 and comp == 1:
    print('Você ganhou')
elif mao == 2 and comp == 3:
    print('Você perdeu')
elif mao == 3 and comp == 1:
    print('Você perdeu')
elif mao == 3 and comp == 2:
    print('Você ganhou')