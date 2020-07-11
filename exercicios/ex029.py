print('---CONDIÇÃO SIMPLES---')
v = float(input('Digite a maior velocidade atingida pelo carro: '))
print('-=-'*20)
multa = (v - 80) * 7
if v > 80:
    print('Você excedeu a velocidade permitida!')
    print('-=-'*20)
    print('Sua multa é de R${:.2f}'.format(multa))
print('---FIM---')
