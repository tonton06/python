print('-'*30)
print('COMPARADOR DE NÚMERO INTEIROS')
print('-'*30)
n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
print('-'*30)
if n1 > n2:
    print('O primeiro número é MAIOR!'.format(n1, n2))
elif n2 > n1:
    print('O segundo número é MAIOR!'.format(n2, n1))
else:
    print('NÃO EXISTE valor maior, os dois são iguais!')
print('-'*30)
