nome = str(input('Digite seu nome completo: ')).strip().title()
s = nome.split()
print(nome)
print('Muito prazer em te conhecer, {}!'.format(s[0]))
print('Seu primeiro nome é {}'.format(s[0]))
print('Seu último nome é {}'.format(s[-1]))

