num = ()
pares = ()

for times in range(1, 5):
    
    value = int(input('Digite um número: '))
    tuple = (value,)

    num += tuple

    if value % 2 == 0:
        pares += tuple

print(f'O número 9 apareceu {num.count(9)} vezes')

if 3 in num:
    print(f'O número 3 foi o {num.index(3) + 1}° a ser digitado')
else:
    print('O número 3 não foi digitado')

print('Os números pares são ',end='')
for count in pares:
    print(count, end=' ')
    