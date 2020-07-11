print('Uma loja está com 5% de desconto em seus produtos')
p = float(input('Escreva o preço do produto que você procura: R$'))
e = p - (p * 5) / 100
print('Seu produto está saindo por R${:.2f}!'.format(e))


