n = int(input('Digite um número inteiro: '))
for c in range(11):
    print('{} x {:>2} = {:>2}'.format(n, c, n * c))
