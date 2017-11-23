#EXERCICIO 63
print('-='*20)
print('Lembrando da sequencia de Fibonacci')
print('-='*20)
qts = int(input('Quantos números da sequência? '))
cont = 0
n_ant = 1
n_novo = 1
fib = n_ant + n_novo
while cont < qts:
    print(fib)
    cont += 1
