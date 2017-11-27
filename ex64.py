print('-='*16)
print('Para sair digite 999')
print('-='*16)
num = 0
cont = 0
soma = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        cont += 1

print('os números digitados {} vezes somam um total de {}.'.format(cont, soma))