values = []
biggest = []
smallest = []

for count in range(0, 5):
    values.append(int(input('Digite um número: ')))

for position, value in enumerate(values):

    if value == max(values):
        biggest.append(str(position))
    elif value == min(values):
        smallest.append(str(position))

join_biggest = '...'.join(biggest)
join_smallest = '...'.join(biggest)

print(f'Números digitados: {values}')
print(f'O MENOR número digitado foi {min(values)} que está nas posições {join_smallest}')
print(f'O MAIOR número digitado foi {max(values)} que está nas posições {join_biggest}')
