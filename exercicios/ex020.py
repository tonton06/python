from random import sample
n1 = input('Primeiro aluno: ').strip().title()
n2 = input('Segundo aluno: ').strip().title()
n4 = input('Terceiro aluno: ').strip().title()
n3 = input('Quarto aluno: ').strip().title()
list = [n1, n2, n3, n4]
r = sample(list, 4)
print(r)
