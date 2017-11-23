num = int(input('Digite um número para ver sua tabuada: '))
a = 1
for c in range(1,11):
    if a <= 10:
        print('{} x {} = {}'.format(num,a,num*a))
        a = a + 1