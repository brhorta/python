from datetime import date
ano = int(input('Qual seu ano de nascimento? '))
hoje = date.today()
anoAtual = hoje.year
idade = anoAtual - ano
tempo = 0

if idade == 18:
    print('Está na hora de se alistar')
elif idade < 18:
    tempo = 18 - idade
    print('Você ainda vai se alistar daqui a {} anos'.format(tempo))
elif idade > 18:
    tempo = idade - 18
    print('Já passou o tempo do alistamento faz {} anos'.format(tempo))