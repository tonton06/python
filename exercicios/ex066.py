print('-'*50)
print('|DESCONSIDERANDO O FLAG 2.0|')
print('-'*50)

count = sum = 0

while True:
    
    num = int(input('[ 999 ] Sair | Digite um número: '))
    
    if num == 999:
        break

    count += 1
    sum += num

print(f'Foram digitados {count} números e sua soma é {sum}')

# count = -1
# sum = 0
# While num != 999:
#    count += 1
#    sum += num
#    num = int(input('Digite um número [ 999 ] Sair: '))
