from time import sleep
print('--'*30)
print('DESCONSIDERANDO O FLAG')
print('--'*30)

count = -1
sum = 0
num = 0

while num != 999:
    
    sum += num
    count += 1

    num = int(input('[ 999 ] Parar\nDigite um número inteiro: '))

print('--'*30)
print('Foram digitados {} números e a soma entre eles foi de {}'.format(count, sum))
print('--'*30)
sleep(2)
