n = s = 0
cont = 0
while True:
    n = int(input('Digite um número(999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
#abaixo a F string do novo python 3,6
print(f'A soma dos {cont} valores foi {s}!')