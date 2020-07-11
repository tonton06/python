from math import sqrt
co = float(input('Valor do cateto oposto: '))
ca = float(input('Valor do cateto adjacente: '))
h2 = (co ** 2) + (ca ** 2)
h = sqrt(h2)
print('A hipotenusa desse triângulo vale {:.2f}'.format(h))



# = hypot(co, ca)
