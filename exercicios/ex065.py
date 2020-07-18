print('--'*30)
print('Média, Maior, Menor e Saída')
print('--'*30)

count = 0
sum = 0
choice = 2

while choice > 0:

    num = int(input('Digite um número inteiro: '))

    if count == 0:
        biggest = num
        smallest = num
    else:
        if num > biggest:
            biggest = num
        elif num < smallest:
            smallest = num
    
    sum += num
    count += 1
    choice = 2
    while choice != 0 and choice != 1:
        choice = int(input('[ 1 ] Continuar\n[ 0 ] Sair\nEscolha: '))

print('A média dos {} números Digitados é {:.2f}'.format(count, (sum) / (count)))
print('O Maior número foi {} e o Menor foi {}'.format(biggest, smallest))
