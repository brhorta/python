print('-='*20)
print('Lembrando da sequencia de Fibonacci')
print('-='*20)
n = int(input('Quantos números da sequência? '))
cont = 0
ant = 0
prox = 1
while cont < n:
    if cont == 0:
        print('{}, '.format(cont),end='')
    print('{}, '.format(prox), end='')
    fib = ant
    ant = prox
    prox = fib + ant
    cont += 1

