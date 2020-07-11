print('--'*15)
print('CONDIÇÃO DE PAGAMENTO')
print('--'*15)
price = float(input('Digite o preço do PRODUTO: '))
print('-=-'*15)
print('FORMA DE PAGAMENTO')
print('[ 1 ] À VISTA NO DINHEIRO / CHEQUE ')
print('[ 2 ] À VISTA NO CARTÃO')
print('[ 3 ] EM 2x NO CARTÃO ')
print('[ 4 ] EM 3X ou MAIS NO CARTÃO ')
pay = int(input('Escolha sua forma de pagamento: '))
print('-=-'*15)
if pay == 1:
    juros = price - (price * 10 / 100)
    print('Você recebeu 10% de desconto, o novo preço é R${:.2f}'.format(juros))
elif pay == 2:
    juros = price - (price * 5 / 100)
    print('Você recebeu 5% de desconto, o novo PREÇO é R${:.2f}'.format(juros))
elif pay == 3:
    print('Sua compra será realizada em 2x de R${:.2f}'.format(price / 2))
    print('Seu preço não sofreu alteração, R${:.2f}'.format(price))
elif pay == 4:
    p_juros = (price + price * 20 / 100)
    parcelas = int(input('Em quantas vezes você quer parcelar? '))
    print('serão {}x de R${:.2f}'.format(parcelas, p_juros / parcelas))
    print('Seu produto sairá (COM JUROS) por R${:.2f}'.format(p_juros))
else:
    print('\033[31mNÃO HÁ ESTA OPÇÃO DE PAGAMENTO!\033[m')
print('-=-'*15)
