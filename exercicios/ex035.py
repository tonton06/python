print('-=-' * 15)
print('ANALIZADOR DE TRIÂNGULOS')
print('-=-' * 15)
l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print('Um triângulo PODE ser formado com esses valores!')
else:
    print('Um triângulo NÃO PODE ser formado com esses valores!')
