print('--'*15, '\033[32m')
print('MÉDIA')
print('\033[m-=-'*15, '\033[34m')
note1 = float(input('Digite a primeira nota: '))
note2 = float(input('Digite a segunda nota: '))
print('\033[m--'*15)
m = (note1 + note2) / 2
print('--'*15, '\033[31m')
if m < 5:
    print('Sua média foi {:.1f}, você está REPROVADO!'.format(m))
elif m >= 5 and m < 7:
    print('Sua média foi {:.1f}, você está de RECUPERAÇÃO'.format(m))
else:
    print('Sua média foi {:.1f}, você PASSOU'.format(m))
print('\033[m--'*15)
