#EXERCÍCIO 61
print('Exercício de P.A. (Progressão Aritmética)')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de uma P.A.: '))
soma = 0
resp = pt
while soma < 10:
    soma += 1
    print('{}'.format(resp), end=' -> ')
    resp = pt + razao * soma
print('ACABOU')
