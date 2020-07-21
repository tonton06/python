teams = ('Flamengo - RJ', 'Santos - SP', 'Palmeiras - SP', 'Grêmio - RS', 'Athletico Paranaense - PR', 'São Paulo - SP',
         'Internacional - RS', 'Corinthians - SP', 'Fortaleza - CE', 'Goiás - GO', 'Bahia - BA', 'Vasco da Gama - RJ',
         'Atlético - MG', 'Fluminense - RJ', 'Botafogo - RJ', 'Ceará - CE', 'Cruzeiro - MG', 'Csa - AL', 'Chapecoense - SC',
         'Avaí - SC')

print(teams)

print('='*30)

for count, names in enumerate(teams[:5]):
    print(f'{count + 1}°', end=' ')
    print(names)

print('='*30)

for count, names in enumerate(teams[-4:]):
    print(f'{teams.index(names) + 1}°', end=' ')
    print(names)

print('='*30)

print(f'{sorted(teams)}')

print('='*30)

print('A Chapecoense está na {}° colocação'.format(teams.index('Chapecoense - SC') + 1))
