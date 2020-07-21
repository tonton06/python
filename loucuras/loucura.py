print('='*30)
print('PRODUTOS NOTÁVEIS')
print('='*30)

calc = 0
while calc > 2 or calc < 1:
    calc = int(input('[ 1 ] Soma dos quadrados\n[ 2 ] Diferença dos quadrados\nEscolha: '))

num = (str(input('Primeiro valor: ')), str(input('Segundo valor: ')))

if calc == 1:
    print('{}² + 2{}{} + {}²'.format(num[0], num[0], num[1], num[1]))
elif calc == 2:
    print('{}² - 2{}{} + {}²'.format(num[0], num[0], num[1], num[1]))
