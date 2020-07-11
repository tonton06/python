print('--'*15)
print('ANALIZADOR DE TRIÂNGULOS V2')
print('--'*15)
v1 = float(input('Digite o valor do primeiro lado: '))
v2 = float(input('Digite o valor do segundo lado: '))
v3 = float(input('Digite o valor do terceiro lado: '))
print('-=-'*15)
if v1 + v2 > v3 and v1 + v3 > v2 and v3 + v2 > v1:
    if v1 == v2 and v1 == v3:
        print('O Triângulo formado é EQUILÁTERO!')
    elif v1 == v2 or v2 == v3 or v3 == v1:
        print('O Triângulo formado é ISÓCELES')
    else:
        print('O Triângulo formado é ESCALENO')
else:
    print('NÃO É POSSÍVEL FORMAR UM TRIÂNGULO COM ESSES VALORES!!')
print('-=-'*15)
