t = 0
s = 0
for c in range(1,500):
    if c % 3 == 0 and c % 2 != 0:
        print(c)
        s += c
        t += 1
print('A soma de todos os {} valores solicitados é {}'.format(t,s))