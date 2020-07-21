from random import randint

tuple = ()

for count in range(5):
    random = (randint(1, 10),)
    tuple += random

print(tuple)
print(f'O menor número foi {min(tuple)}')
print(f'O maior número foi {max(tuple)}')
