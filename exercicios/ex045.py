from random import choice
from time import sleep
print('\033[34m-=-'*15)
print('JOKENPÔ')
print('-=-'*15)
print('VOCÊ vai jogar jokenpô com o computador!')
list = [1, 2, 3]
pc = choice(list)
print('-=-'*15)
print('\033[31m-=-'*15)
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
player = int(input('Escolha sua jogada: '))
print('-=-'*15)
print('\033[30m-=-'*15)
print('O computador está pensando...')
print('-=-'*15)
sleep(3)
print('\033[32m-=-'*15)
if pc == player:
    if pc == 1:
        print('O COMPUTADOR ESCOLHEU PEDRA')
    elif pc == 2:
        print('O COMPUTADOR ESCOLHEU PAPEL')
    elif pc == 3:
        print('O COMPUTADOR ESCOLHEU TESOURA')
    print('-=-'*15)
    print('EMPATE')
elif pc == 1 and player == 3 or pc == 2 and player == 1 or pc == 3 and player == 2:
    if pc == 1:
        print('O COMPUTADOR ESCOLHEU PEDRA')
    elif pc == 2:
        print('O COMPUTADOR ESCOLHEU PAPEL')
    elif pc == 3:
        print('O COMPUTADOR ESCOLHEU TESOURA')
    print('-=-'*15)
    print('VOCÊ PERDEU')
elif player == 1 and pc == 3 or player == 2 and pc == 1 or player == 3 and pc == 2:
    if pc == 1:
        print('O COMPUTADOR ESCOLHEU PEDRA')
    elif pc == 2:
        print('O COMPUTADOR ESCOLHEU PAPEL')
    elif pc == 3:
        print('O COMPUTADOR ESCOLHEU TESOURA')
    print('-=-'*15)
    print('VOCÊ GANHOU')
else:
    print('NÃO HÁ ESSA OPÇÃO')
print('-=-'*15)
