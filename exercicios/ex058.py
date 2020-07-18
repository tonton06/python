from random import randint
pc = randint(0,10)

print('--'*15)
print('De 0 a 10, tente adivinhar o número que o computador pensou')
print('--'*15)

count = 0
num = 11

while num != pc:
    num = int(input('Faça sua escolha: '))
    count += 1

    if num != pc:
        if pc - num > 0:
            print('\033[34mMais...\033[m')
        if pc - num < 0:
            print('\033[32mMenos...\033[m')

print('--'*15)
print('\033[35mVocê acertou em {} tentativas'.format(count))
print('--'*15)
