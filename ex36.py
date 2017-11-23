casa = int(input('Qual é o valor do imóvel? '))
sal = int(input('Qual é o valor total do seu salário atual? '))
anos = int(input('Quantos anos pretende pagar o imóvel? '))

trinta = sal * 0.3
meses = anos * 12
parcela = casa / meses

if parcela > trinta:
    print('Desculpe, seu empréstimo foi negado.')
else:
    print("Parabéns!\nSeu emprestimo foi aprovado!\nEste imóvel será seu por {} prestações de R$ {}.".format(meses, round(parcela,2)))