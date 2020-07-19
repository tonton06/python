from time import sleep

count_age = count_sex = count_girl = 0

while True:    
    
    print('='*50)
    print('{:^50}'.format('CADASTRE UMA PESSOA'))
    print('='*50)

    age = int(input('Idade: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('sexo: [M/F] ')).strip().capitalize()[0]   
    print('='*50)

    if age > 18:
        count_age += 1
    if sex in 'M':
        count_sex += 1
    if sex in 'F' and age < 20:
        count_girl += 1

    choice = ' '
    while choice not in 'SN':
        choice = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if choice == 'N':
        break

print('='*50)
print(f'{count_age} pessoas tem mais de 18 anos!')
print(f'{count_sex} pessoas são do sexo masculino!')
print(f'{count_girl} Mulheres tem menos de 20 anos!')
print('='*50)
