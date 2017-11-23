from datetime import date
anoNasc = int(input('Qual seu ano de nascimento? '))
hoje = date.today()
anoAtual = hoje.year
cat = anoAtual - anoNasc

if cat <= 9:
    print('MIRIM')
elif cat > 9 and cat < 14:
    print('INFANTIL')
elif cat > 14 and cat < 19:
    print('JUNIOR')
elif cat > 19 and cat <= 20:
    print('MASTER')
elif cat > 21:
    print('SENIOR')