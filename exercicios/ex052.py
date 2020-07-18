num = int(input('Digite um número inteiro: '))
s = 0
cont = 0
for c in range(1, num + 1):
    d = num % c
    if d == 0:
        if c == num:
            print('\033[34m{}'.format(c), '\n')
        else:
            print('\033[34m{}'.format(c), end=' - ')
    elif d != 0:
        print('\033[31m{}'.format(c), end=' - ')
    if d == 0:
        cont += 1
print('\033[m')
if cont == 2:
    print('Número Primo')
else:
    print('Número não Primo')
