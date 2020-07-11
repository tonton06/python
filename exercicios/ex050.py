s = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    d = num % 2
    if d == 0:
        s = s + num
print(s)
