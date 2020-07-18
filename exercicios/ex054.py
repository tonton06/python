from datetime import date
cont = 0
cont2 = 0
for c in range(1, 8):
    year = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    age = date.today().year - year
    if age >= 21:
        cont += 1
print('\n\033[32m{} pessoas são MAIORES de idade\n\033[31m{} pessoas são MENORES de idade'.format(cont, c - cont))
