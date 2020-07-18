s = 0
s2 = 0
cont = 0
cont2 = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    d = num % 2
    if d == 0:
        s += num
        cont += 1
    else:
        s2 += num
        cont2 += 1
print('São {} números PARES e sua soma é {}'.format(cont, s))
print('São {} números Ímpares e sua soma é {}'.format(cont2, s2))
