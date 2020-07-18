sex = ''

while sex != 'F' and sex != 'M':
    
    print('--'*8)
    sex = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('--'*8)
    
    if sex != 'F' and sex != 'M':
        print('\033[31mTente novamente\033[m')

print('FIM')
