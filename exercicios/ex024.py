cid = str(input('Digite o nome de uma cidade: ')).strip().title()
r = (cid.split())
print('{} tem como primeira palavra "Santo" --- {}'.format(cid, 'Santo' in r[0]))
