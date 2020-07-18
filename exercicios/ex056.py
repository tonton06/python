name = ''
oldest = 0
sum = 0
count = 0
count_m = 0
for c in range(1, 5):
    
    print('\033[34m---- {}° Pessoa  ----'.format(c))
    input_name = str(input('Nome: ')).strip().capitalize()
    age = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    
    sum += age
    
    if sex == 'M' or sex[0] == 'M':
        count_m += 1
        if age > oldest:
            oldest = age
            name = input_name

    if sex == 'F' or sex[0] == 'F':
        if age < 20:
            count += 1

print('\033[32mA média de idade do grupo é {}'.format(sum / 4))
if count_m == 0:
    print('Não há homens no grupo!')
else:    
    print('O Homem mais velho do grupo é {} que tem {} anos'.format(name, oldest))
print('Das mulheres do grupo, {} tem menos de 20 anos!'.format(count))
        