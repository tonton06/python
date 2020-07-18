from time import sleep
print('-'*50)
print('|SEQUÊNCIA DE FIBONACCI|')
print('-'*50)

num = int(input('Quantidade de Termos: '))

first = 0
second = 1
count = num - 1

print('-'*50)
print('{} - {} '.format(first, second), end='')

while count > 1:
    count -= 1
    value = first + second
    first = second
    second = value
    print('- {} '.format(value), end='')

print('')
print('-'*50)
print('Finalizando Programa...')
print('-'*50)
sleep(2)
