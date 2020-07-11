d = int(input('Dias alugado: '))
km = float(input('Quilômetros rodados: '))
pd = d * 60
pkm = km * 0.15
print('Seu carro foi alugado por {} dias e percorreu {:.1f}km!'.format(d, km))
print('Isso equivale a R${:.2f}'.format(pd + pkm))
