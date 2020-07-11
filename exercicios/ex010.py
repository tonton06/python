print('Esse programa mostra quantos dólares uma pessoa pode comprar com uma quantidade X de reais')
r = float(input('Quantos reais você tem na carteira? R$'))
d = r / 5.48
e = r / 6.15
print('Com R${:.2f} você pode comprar ${:.2f} ou {:.2f} €'.format(r, d, e))
