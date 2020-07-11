s = float(input('Valor do salário: R$'))
if s > 1250:
    print('Seu aumento foi de R${:.2f}'.format(s * 10 / 100 + s))
else:
    print('Seu aumento foi de R${:.2f}'.format(s * 15 / 100 + s))
