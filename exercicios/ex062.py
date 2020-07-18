from time import sleep
print('-'*50)
print('PA')
print('-'*50)

print('')
print('-'*50)

sum = int(input('valor inicial: '))
skip = int(input('Razão: '))

count = 10
choice = -1

while choice != 0:

    if choice == 1:
        count = int(input('Quantidade de termos: '))
   
    print('-'*50)
   
    while count > 0:

        print('| {} '.format(sum), end='')
        count -= 1
        sum += skip
    
    print('')
    print('-'*50)

    choice = int(input('\n[ 1 ] Mais termos\n[ 0 ] Sair\nEscolha: '))

print('-'*50)
print('FINALIZANDO PROGRAMA...')
print('-'*50)

sleep(2)
