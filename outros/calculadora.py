from math import sin, cos, tan, radians
print('\033[30m-=-'*15)
print('CALCULADORA')
print('-=-' * 15, '\033[38m')
print('\033[34m-=-'*15)
print('[ 1 ] SOMA')
print('[ 2 ] SUBTRAÇÃO')
print('[ 3 ] MULTIPLICAÇÃO')
print('[ 4 ] DIVISÃO')
print('[ 5 ] POTENCIAÇÃO')
print('[ 6 ] RAIZ')
print('[ 7 ] MÉDIA')
print('[ 8 ] PORCENTAGEM')
print('[ 9 ] CONVERSÃO TEMPERATURA')
print('[ 10] SENO - COSSENO - TANGENTE')
print('-=-'*15, '\033[32m')
print('-=-'*15)
c = int(input('Escolha a operação: '))
print('-=-'*15, '\033[31m')
print('-=-'*15)
if c == 1:
    soma1 = float(input('Digite a primeira PARCELA: '))
    soma2 = float(input('Digite a segunda PARCELA: '))
    print('{} + {} = {}'.format(soma1, soma2, soma1 + soma2))
elif c == 2:
    sub1 = float(input('Digite o MINUENDO: '))
    sub2 = float(input('Digite o SUBTRAENDO: '))
    print('{} - {} = {}'.format(sub1, sub2, sub1 - sub2))
elif c == 3:
    mult1 = float(input('Digite o MULTIPLICANDO: '))
    mult2 = float(input('Digite o MULTIPLICADOR: '))
    print('{} x {} = {}'.format(mult1, mult2, mult1 * mult2))
elif c == 4:
    div1 = float(input('Digite o DIVIDENDO: '))
    div2 = float(input('Digite o DIVISOR: '))
    print('{} : {} = {}'.format(div1, div2, div1 / div2))
elif c == 5:
    pow1 = float(input('Digite a BASE: '))
    pow2 = float(input('Digite o EXPOENTE: '))
    print('{} elevado a {} = {}'.format(pow1, pow2, pow1 ** pow2))
elif c == 6:
    raiz1 = float(input('Digite o valor da ÍNDICE: '))
    if raiz1 == 2:
        raiz2 = float(input('Digite o valor da RADICANDO: '))
        print('A raiz quadrada de {} = {:.2f}'.format(raiz2, raiz2 ** (1/2)))
    elif raiz1 == 3:
        raiz2 = float(input('Digite o valor do RADICANDO: '))
        print('A raiz cúbica de {} = {:.2f}'.format(raiz2, raiz2 ** (1/3)))
    else:
        print('\033[30mESTA PARTE AINDA NÃO FOI PROGRAMADA, POR FAVOR TENTE OUTRA OPERAÇÃO!!')
elif c == 7:
    num = int(input('Digite a quantidade de valores: '))
    if num == 2:
        med1 = float(input('Digite o primeiro valor: '))
        med2 = float(input('Digite o segundo valor'))
        print('A MÉDIA entre {} e {} = {:.1f}'.format(med1, med2, (med1 + med2) / 2))
    elif num == 3:
        med1 = float(input('Digite o primeiro valor: '))
        med2 = float(input('Digite o seundo valor: '))
        med3 = float(input('Digite o terceiro valor: '))
        print('A MÉDIA entre {} , {} e {} = {:.1f}'.format(med1, med2, med3, (med1 + med2 + med3) / 3))
    elif num == 4:
        med1 = float(input('Digite o primeiro valor: '))
        med2 = float(input('Digite o segundo valor: '))
        med3 = float(input('Digite o terceiro valor: '))
        med4 = float(input('Digite o quarto valor: '))
        print('A MÉDIA entre {} , {} , {} , e {:.1f} é {}'.format(med1, med2, med3, med4, (med1 + med2 + med3 + med4) / 4))
    else:
        print('\033[30mESTA PARTE AINDA NÃO FOI PROGRAMADA, POR FAVOR TENTE OUTRA OPERAÇÃO!!')
elif c == 8:
    porc1 = float(input('Digite a PORCENTAGEM requerida: '))
    porc2 = float(input('Digite o valor para ser obtida a PORCENTAGEM: '))
    print('{}% de {} = {:.2f}'.format(porc1, porc2, porc2 * porc1 / 100))
elif c == 9:
    print('Celsius - Fahrenheit 1')
    print('Fahrenheit - Celsius 2')
    graus = int(input('Digite: '))
    if graus == 1:
        graus = float(input('Digite o valor da temperatura em GRAUS: '))
        print('{}° equivale a {:.1f}f°'.format(graus, (graus * 9) / 5 + 32))
    elif graus == 2:
        fah = float(input('Digite o valor da temperatura em FAHRENHEIT: '))
        print('{}F° equivale a {:.1f}°'.format(fah, (fah - 32) * 5 / 9))
    else:
        print('-=-'*15)
        print('\033[30m-=-'*15)
        print('ESTA PARTE AINDA NÃO FOI PROGRAMADA, POR FAVOR TENTE OUTRA OPERAÇÃO!!')
elif c == 10:
    ang = float(input('Digite o valor do ÂNGULO: '))
    rad = radians(ang)
    print('SENO = {:.2f}'.format(sin(rad)))
    print('COSSENO = {:.2f}'.format(cos(rad)))
    print('TANGENTE = {:.2f}'.format(tan(rad)))
else:
    print('\033[30mESTA PARTE AINDA NÃO FOI PROGRAMADA, POR FAVOR TENTE OUTRA OPERAÇÃO!!')
print('-=-'*15, '\033[m')
