while True:
    t = int(input('Quer ver a tabuada de qual valor? '))
    num = 1
    mult = t * num
    if t < 0:
        break
    print('-'*20)
    while True:
        print(f'{t} x {num} = {mult}')
        if num == 10:
            break
        num += 1
        mult = t * num
    print('-'*20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')