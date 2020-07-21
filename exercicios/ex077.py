tuple = ('Bola', 'Cachorro', 'Gato', 'Cavalo', 'Computador', 'Desenvolvimento')

for word in tuple:

    vogal = ()
    print(f'\nAs vogais de {word.upper()} são ', end='')
    
    for count, letter in enumerate(word):
        
        if letter.lower() in 'aeiou':
            print(letter.upper(), end=' ')

# def format_tuple(tuple):
#     result = ''
#     for name in tuple:
#         result += f'{name} '
#     return result

# tuple = ('Bola', 'Cachorro', 'Gato', 'Cavalo', 'Computador', 'Desenvolvimento')

# for word in tuple:

#     vogal = ()
#     for count, letter in enumerate(word):

#         if letter in 'AaEeIiOoUu':
#             vogal += (letter, )

#     print(f'As vogais de {word} são {format_tuple(vogal)}')
