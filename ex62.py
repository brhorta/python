#EXERCÍCIO 62
print('Exercício de P.A. (Progressão Aritmética)')
pt = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão de uma P.A.: '))
soma = 0
resp = pt
mais = 'N'
qts = 0
zero = 0
while soma < 10:
    soma += 1
    print('{}'.format(resp), end=' -> ')
    resp = pt + razao * soma
    if soma == 10:
        mais = str(input('MOSTRAR MAIS TERMOS? [S/N]')).upper()
        if mais == 'S':
            qts = int(input('Quantos? '))
            while zero < qts:
                print('{}'.format(resp), end=' -> ')
                zero += 1
                resp = resp + razao
print('ACABOU')
