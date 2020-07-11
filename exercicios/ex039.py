from datetime import date
print('--'*15)
atual = date.today().year
print('ALISTAMENTO')
print('--'*15)
ano = int(input('Digite seu ano de nascimento: '))
print('[ 1 ] Sexo MASCULINO')
print('[ 2 ] Sexo FEMININO')
sex = int(input('Escolha seu sexo: '))
print('--'*15)
if sex == 1:
    if ano < atual - 18:
        if ano == atual - 19:
            print('Falta 1 ano para o seu ALISTAMENTO')
        elif ano < atual - 19:
            print('Faltam {} anos para o seu ALISTAMENTO'.format(2002 - ano))
    elif ano > atual - 18:
        if ano == atual - 17:
            print('Já se passou 1 anos desde seu ALISTAMENTO')
        elif ano > atual - 17:
            print('Já se passaram {} anos desde seu ALISTAMENTO'.format(ano - 2002))
    else:
        print('Você deve fazer seu ALISTAMENTO OPCIONAL OBRIGATÓRIO IMEDIATAMENTE!')
elif sex == 2:
    print('Seu ALISTAMENTO é opcional!')
print('--'*15)
