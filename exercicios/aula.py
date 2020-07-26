# # modifie

num = [1, 2, 3]
num[2] = 1
print

# # add

animais = ['cachorro', 'gato', 'galo']
animais.append('Leão')
animais.insert(0, 'Jaguatirica')

# # remove

animais.pop()
del animais[2]
lanche.remove('cachorro')

# # verification

if 'cachorro' in animais:
    animais.remove('cachorro')

# function list

values = list(range(1, 11))

# # sorting

values = [1, 2, 5, 4, 9, 8, 10]
values.sort()
valores.sort(reverse=True)

# # counting

values = [1, 2, 5, 4, 9, 8, 10]
len(values)

# input

valores = []
valores.append(int(input('Digite um número: ')))
print(valores)

# for

values = [2, 4, 6, 8, 10, 12]
for position, value in enumerate(values):
    print(f'Na posição {position} encontrei o valor {value}')

# python only

a = [1, 2, 3, 4]
b = a

!=!=!=!=!=!=!=!=

a = [1, 2, 3, 4]
b = a[:]
