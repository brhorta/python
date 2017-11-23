from math import factorial
num = 0
fat = 0
num = int(input('Digite um número: '))
fat = num
print('{}!='.format(num),end='')
while num != 0:
    print('{}'.format(num),end='x')
    num -= 1
    if num == 1:
        print('{}'.format(num),end='=')
        num = 0
print('{}'.format(factorial(fat)))

