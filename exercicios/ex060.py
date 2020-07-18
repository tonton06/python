print('--'*15)
print('FATORIAL')
print('--'*15)

num = int(input('Digite um número: '))
print('--'*15)

count = num
print('{}! = '.format(num), end='')

while count > 0:
    
    if count == 1:
        print('{} = {}'.format(count, num))
    else:    
        print('{} x '.format(count), end='')
    
    count -= 1
    num *= count

###For
###num = int(input('Digite um número: '))
###
###print('{}! = '.format(num), end='')
###for count in range(num, 1, -1):
###    
###    if count == 1:
###        print('{} = '.format(count), end='')
###
###    else:
###        print('{} x '.format(count), end='')
###
###    num *= count - 1
###
###print('{}'.format(num))
