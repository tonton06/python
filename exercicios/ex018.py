from math import sin, tan, cos, radians
a = float(input('Digite a medida do ângulo: '))
g = radians(a)
sen = sin(g)
cos = cos(g)
tan = tan(g)
print('O SENO é {:.2f}'.format(sin))
print('O COSSENO é {:.2f}'.format(cos))
print('A TANGENTE é {:.2f}'.format(tan))
