print('='*50)
print('{:^50}'.format('Loja Descontão'))

count = count_price = total = cheeper = cheeper_name = 0

while True:
    
    print('='*50)
    print('{:^50}'.format('Produto'))
    print('='*50, '')


    name = str(input('Nome do produto: ')).strip().capitalize()
    price = float(input('Preço do produto: R$'))
    print('='*50)
    
    total += price
    count += 1
    
    if price > 1000:
        count_price += 1
    
    if count == 1 or price < cheeper:
        cheeper = price
        cheeper_name = name
#    elif count > 1:
#        if price < cheeper:
#            cheeper = price
#            cheeper_name = name

    choice = '.'
    while choice not in 'SN':
        choice = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if choice == 'N':
        break

print('='*50)
print(f'O total foi de R${total:.2f}')
print(f'{count_price} Produtos custam mais de R$1000.00')
print(f'{cheeper_name} foi o produto mais barato, custando R${cheeper:.2f}')
print('='*50)
