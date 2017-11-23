n1 = int(input('Digite o primeiro numero '))
n2 = int(input('Digite o segundo numero '))

if n1 > n2:
    print('{} é maior'.format(n1))
elif n2 > n1:
    print('{} é maior'.format(n2))
elif n2 == n1:
    print('Não existe valor maior, os dois numeros sao iguais')