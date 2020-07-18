frase = str(input('Digite uma frase: ')).strip().lower()
join = frase.replace(' ', '')
reverse = join[::-1]
print('O inverso de {} é {}'.format(join, reverse))
if join == reverse:
    print('A frase digitada é um PALÍNDROMO')
else:
    print('A frase digitada não é um PALÍNDROMO')
