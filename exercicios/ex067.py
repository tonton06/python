from time import sleep
print('='*50)
print('TABUADA V.3')
print('='*50)

while True:  

    num = int(input('{ número negativo } Sair | Digite um número: '))
    if num < 0:
        break

    print('='*50)

    for count in range(count, 10):
        print(f'{num:>2} x {count:>2} = {num * count:>2}')

    print('='*50)

print('='*50)
print('FINALIZANDO PROGRAMA...')
print('='*50)
sleep(2)
