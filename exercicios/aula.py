# lanche = ['cachorro', 'gato', 'galo']
# print(lanche)

# lanche.append('Cocrodilo')
# print(lanche)

# lanche.insert(1, 'Golira')
# print(lanche)

# del lanche[1]
# print(lanche)

# lanche.pop(0)
# print(lanche)

# lanche.remove('gato')
# print(lanche)

#===================================#

# if 'Golira' in lanche:
#     lanche.remove('Golira')

# valores = [8, 2, 3, 6, 2, 9]
# print(valores)

# valores.sort()
# print(valores)

# valores.sort(reverse=True)
# print(valores)

# len(valores)
# print(valores)

# num = [1, 3, 5, 2, 8]
# for pos, valores in enumerate(num):
#     print(f'Posição {pos + 1} num {valores}')

a = [1, 2, 3, 4]
b = a
b.append(5)
print(f'Lista 1 = {a}')
print(f'Lista 2 = {b}')

a = [1, 2, 3, 4]
b = a[:]
b.append(5)
print(f'Lista 1b {a}')
print(f'Lista 2b {b}')
