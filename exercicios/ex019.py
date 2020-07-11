from random import choice
n1 = str(input('Nome do primeiro aluno: ')).strip().title()
n2 = str(input('Nome do segundo aluno: ')).strip().title()
n3 = str(input('Nome do terceiro aluno: ')).strip().title()
n4 = str(input('Nome do quarto aluno: ')).strip().title()
lista = [n1, n2, n3, n4]
r = choice(lista)
print('O aluno escolhido foi {}'.format(r))
