values = []
choice = ' '

while choice != 'N':
    num = int(input('Digite um número: '))
    values.append(num)

    choice = ' '
    while choice not in 'SN':
        choice = str(input('Continuar? [S/N] ')).upper().strip()[0]

values.sort(reverse=True)

print(f'Você digitou {len(values)} números')
print(f'Lista em ordem decrescente: {values}')

if 5 in values:
    print(f'O número 5 se encontra na posição {values.index(5) + 1}')
else:
    print('Número 5 não encontrado!')
