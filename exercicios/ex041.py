from datetime import date
actual = date.today().year
print('--'*15)
print('CONFEDERAÇÃO DE NATAÇÃO')
print('--'*15)
ano = int(input('Digite o ano do seu nascimento: '))
idade = actual - ano
print('--'*15)
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JUNIOR')
elif idade == 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
print('--'*15)
