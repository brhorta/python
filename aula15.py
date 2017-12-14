n = s =0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
#abaixo a F string do novo python 3,6
print(f'Total deu {s}')
