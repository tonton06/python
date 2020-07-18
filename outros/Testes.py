#factorial

num = int(input('Digite um número inteiro: '))
print('{}! = '.format(num), end='')
calc = println = num

for count in range(num, 0, -1):
    
    if count == 1:
        print('{}'.format(println), end='')
    elif count > 1:
        print('{} x '.format(println), end='')
    calc *= count
    println -= 1
print(' = {}'.format(calc))
