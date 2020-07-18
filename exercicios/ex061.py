from time import sleep

print('--'*25)
print('PA')
print('--'*25)

valor = int(input('Valor inicial: '))
razao = int(input('Razão: '))

print('--'*25)
conta = 10
soma = valor
print('{}'.format(valor), end='')

while conta != 1:
    
    soma = soma + razao
    conta -= 1
    print(' - {}'.format(soma), end='')

print('')
print('--'*25)
print('FINALIZANDO PROGRAMA...')
print('--'*25)
sleep(2)
