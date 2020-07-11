frase = str(input('Digite uma frase: ')).strip()
join = frase.join
for c in range(join, -1):
    esarf = str(c).strip()
print(frase)
if frase == esarf:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndrmo')
