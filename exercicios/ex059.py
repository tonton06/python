from time import sleep

num_1 = float(input('Primeiro número: '))
num_2 = float(input('Segundo número: '))

choice = 0

while choice != 5:
    
    print('-'*29)
    print('[ 1 ] Soma')
    print('[ 2 ] Multiplicação')
    print('[ 3 ] Maior e Menor')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair')
    
    print('-'*29)
    choice = int(input('Escolha: '))
    print('-'*29)

    if choice == 1:
        print('{} + {} = {}'.format(num_1, num_2, num_1 + num_2))
        
    elif choice == 2:
        print('{} x {} = {}'.format(num_1, num_2, num_1 * num_2))

    elif choice == 3:
        if num_1 - num_2 > 0:
            print('O maior é {} e o Menor é {}'.format(num_1, num_2))
        elif num_2 - num_1 > 0:
            print('O Maior é {} e o Menor é {}'.format(num_2, num_1))
        else:
            print('{} = {}'.format(num_1, num_2))

    elif choice == 4:
        print('>'*7, 'Novos números', '<'*7)
        num_1 = float(input('Primeiro Número: '))
        num_2 = float(input('Segundo Número: '))

    elif choice > 5 or choice < 1:
        print('\033[31mTente novamente!\033[m')
        sleep(2)

print('Saindo do programa...')
print('-'*29)
sleep(2)
