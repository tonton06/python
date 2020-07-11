print('Esse programa calcula a área e diz quantos litros de tinta são necessários para pintar a mesma')
h = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
a = h * l
print('A sua parede tem {:.2f}m² de área '.format(a))
print('Serão necessários {:.2f}L de tinta'.format(a / 2))
