print('{:20}'.format('-='))
print('Você digitará seis valores e eu somarei os pares.')
a = 0
b = 0
num = 0
for c in range(0,6):
#if num % 2 == 0:
    num = int(input('Digite o número para eu somar: '))
    if num % 2 == 0:
        a = num + a
print('O total de números pare é {}.'.format(a))

