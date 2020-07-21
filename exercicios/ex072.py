extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze',
           'quinze', 'dezesseis', 'dezesete', 'dezoito',
           'dezenove', 'vinte')


while True:

    choice = ' '
    num = -1
    
    while num > 20 or num < 0:
        num = int(input('Digite um número inteiro de 0 a 20: '))

    print(f'Você digitou o número {extenso[num]}')
    
    while choice not in 'SN':
        choice = str(input('Continuar? [S/N] ')).strip().upper()[0]
    
    if choice == 'N':
        break
