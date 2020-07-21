products = ('ryzen 3600', 1400.50, 'i5 10400f', 1300.75,
            'GTX 1650 Super', 1350.25, 'GTX 1660 Super', 1980.99)

print('='*60)
print('{:^70}'.format('LISTA'))
print('='*60)

for count, name in enumerate(products):
    
    if count % 2 == 0:
        print(f'{name:.<50}R$', end='')
    elif count % 2 == 1:
        print('{:>8.2f}'.format(name))

print('='*60)
