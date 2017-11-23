z = '-=-'
print('{:.20}'.format(z) )
r1 = float(input('Digite o comprimento da reta 1 '))
r2 = float(input('Digite o comprimento da reta 2 '))
r3 = float(input('Digite o comprimento da reta 3 '))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    if r1 == r2 ==r3:
        print('Parabéns!\nSuas retas formam um triângulo equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Parabéns!\nSuas retas formam um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r3 != r2:
        print('Parabéns!\nSuas retas formam um triângulo escaleno.')
else:
    print('Que pena!\nSuas retas NÃO formam um triângulo.')