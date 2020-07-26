list = []
choice = ' '

while choice != 'N':
    
    num = int(input('Digite um número: '))
    if num not in list:
        list.append(num)
    else:
        print('Número já existente!')

    choice = ' '
    while choice not in 'SN':
        choice = str(input('Continuar? [S/N] ')).upper().strip()[0]
        
print(list, sep=' ')
