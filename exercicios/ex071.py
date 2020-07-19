from time import sleep

print('='*50)
print('{:^50}'.format('CAIXA ELETRÔNICO'))
print('='*50)

valor = int(input('Valor (inteiro) a ser sacado: R$'))

count_50 = count_20 = count_10 = count_1 = 0

while True:

    if valor >= 50:
        count_50 += 1
        valor -= 50
    elif valor >= 20:
        count_20 += 1
        valor -= 20
    elif valor >= 10:
        count_10 += 1
        valor -= 10
    elif valor >= 1:
        count_1 += 1
        valor -= 1
    else:
        break

if count_50 > 0:
    print(f'{count_50} cédulas de 50')
if count_20 > 0:
    print(f'{count_20} cédulas de 20')
if count_10 > 0:
    print(f'{count_10} cédulas de 10')
if count_1 > 0:
    print(f'{count_1} cédulas de 1')

print('='*50)
print('FINALIZANDO PROGRAMA...')
print('='*50)
sleep(2)
