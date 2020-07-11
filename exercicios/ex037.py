print('-'*30)
num = int(input('Digite um número inteiro: '))
print('-'*30)
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
print('-'*30)
choice = int(input('Escolha a base: '))
print('-'*30)
if choice == 1:
    bin_num = bin(num)
    num_str = str(bin_num)
    print('{} em BINÁRIO = {}'.format(num, num_str[2:]))
elif choice == 2:
    octal_num = oct(num)
    octal_str = str(octal_num)
    print('{} em OCTAL = {}'.format(num, octal_str[2:]))
elif choice == 3:
    hex_num = hex(num)
    hex_str = str(hex_num)
    print('{} em HEXADECIMAL = {}'.format(num, hex_str[2:]))
else:
    print('\033[31mNÃO existe esta OPÇÃO')
