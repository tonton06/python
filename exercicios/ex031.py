print('---CONDIÇÃO COMPOSTA---')
d = float(input('Digite a distância da sua viagem: '))
if d <= 200:
    print('Sua passagem custará R${:.2f}'.format(d * 0.5))
else:
    print('Sua passagem custa R${:.2f}'.format(d * 0.45))
