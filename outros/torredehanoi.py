def jogar(n, origem, destino, auxiliar):
    if n > 0:
        jogar(n - 1, origem, auxiliar, destino)
        mover(origem, destino)
        jogar(n - 1, auxiliar, destino, origem)

def mover(origem, destino):
    valor = origem.pop()
    destino.append(valor)

def carregar(n):
    lista = []
    for c in range(n, 0, -1):
        lista.append(c)
    return lista

disk = int(input('Número de discos: '))

origem = carregar(disk)
destino = []
auxiliar = []

print('Auxiliar: ', auxiliar)
print('Origem: ', origem)
print('Destino: ', destino)

print('Aguardando {} jogadas'.format((2 ** len(origem)) - 1))

jogar(len(origem), origem, destino, auxiliar)

print('Origem: ', origem)
print('Destino: ', destino)
print('Auxiliar: ', auxiliar)
