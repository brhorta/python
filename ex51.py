print('Exercício de P.A. (Progressão Aritmética)')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de uma P.A.: '))
decimo = pt + (10 - 1) * razao
for c in range(pt, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('ACABOU')