print('---CONDIÇÃO COMPOSTA + MÓDULOS---')
from random import choice
list = [0, 1, 2, 3, 4, 5]
pc = choice(list)
print('O computador pensou em um número de 0 a 5, tente adivinhar!')
py = int(input('Digite o número: '))
if py == pc:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu, a resposta era {}'.format(pc))
print('---FIM---')
