from datetime import date
ano = int(input('Digite um ano OU digite 0 para ser analizado o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é BISSEXTO!')
else:
    print('Esse ano NÃO é BISSEXTO!')
print('---FIM---')
