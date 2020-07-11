print('-=-'*15)
print('EMPRÉSTIMO BANCÁRIO')
print('-=-'*15)
casa = float(input('Digite o valor da casa: R$'))
sal = float(input('Digite o valor do seu salário: R$'))
time = int(input('Digite em quantos anos você pretende parcelar: '))
mes = time * 12
porc = sal * 30 / 100
prest = casa / mes
if prest > porc:
    print('VERBA INSUFICIENTE')
elif prest <= porc:
    print('EMPRÉSIMO CONCEDIDO')
