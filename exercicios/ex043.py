print('--'*15)
print('IMC')
print('--'*15)
p = float(input('Digite seu peso em KG: '))
a = float(input('Digite sua altura em METROS: '))
imc = p / a ** 2
print('--'*15)
if a > 3:
    print('SUA ALTURA DEVE ESTAR EM METROS')
elif imc < 18.5:
    print('Seu IMC é {:.1f}\n==ABAIXO DO PESO=='.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f}\n==PESO IDEAL=='.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f}\n==SOBREPESO=='.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f}\n==OBESIDADE=='.format(imc))
else:
    print('Seu IMC é {:.2f}\n==OBESIDADE MÓRBIDA=='.format(imc))
print('--'*15)
