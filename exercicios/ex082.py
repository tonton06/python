values = []
odds = []
evens = []
choice = ' '

while choice != 'N':

    num = int(input('Digite um número: '))
    values.append(str(num))

    if num % 2 == 0:
        evens.append(str(num))
    elif num % 2 == 1:
        odds.append(str(num))

    choice = str(input('Continuar? [S/N] ')).upper().strip()[0]

print(f'Números: {"...".join(values)}')
print(f'Números pares: {"...".join(evens)}')
print(f'Números ímpares: {"...".join(odds)}')
