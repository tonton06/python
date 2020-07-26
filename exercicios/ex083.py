expression = []

expression.append(str(input('Digite uma expressão: ')))
count_1 = expression[0].count('(')
count_2 = expression[0].count(')')

if (count_1 + count_2) % 2 == 0:
    print('Em relação a parênteses esta expressão está CORRETA!')
elif (count_1 + count_2) % 2 == 1:
    print('Em relação a parênteses esta expressão está ERRADA!')
