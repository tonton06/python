from random import randint
from time import sleep

print('='*50)
print('PAR OU ÍMPAR')
print('='*50)

count = 0

while True:
   
    print('='*50)    
    print('O computador está pensando...')
    pc = randint(0, 25)
    sleep(2)

    print('='*50)
    side = ' '
    while side not in 'PIÍ':
        side = str(input('[IMPAR/PAR] [I/P] ')).strip().upper()[0]

    player = int(input('Digite seu número: '))
    print('='*50)

    sum = player + pc
    result = sum % 2
    
    print(f'O computador escolheu {pc} e você {player}')
    print('='*50)

    if side == 'I' and result != 0:
            print('\033[32mVocê GANHOU!\033[m')
    elif side == 'P' and result == 0:
            print('\033[32mVocê GANHOU!\033[m')
    else:
        print('\033[31mVocê PERDEU!\033[m')
        break

    count += 1

print('='*50)
print(f'Você conseguiu {count} vitórias consecutivas!')
print('='*50)
print('FINALIZANDO PROGRAMA...')
print('='*50)
sleep(2)
