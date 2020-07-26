def print_option():
    print('[ + ] SOMA')
    print('[ - ] SUBTRAÇÃO')
    print('[ * ] MULTIPLICAÇÃO')
    print('[ / ] DIVISÃO')
    return input('Digite a Expressão: ').split()

def get_value():
    return float(input('Valor: '))

def calc(option, v_1, v_2):
    if option == '+':
       return sum(v_1, v_2)
    elif option == '-':
        return sub(v_1, v_2)
    elif option == '*':
        return mult(v_1, v_2)
    elif option == '/':
        return div(v_1, v_2)

def sum(v_1, v_2):
    return v_1 + v_2

def sub(v_1, v_2):
    return v_1 - v_2

def mult(v_1, v_2):
    return v_1 * v_2

def div(v_1, v_2):
    return v_1 / v_2

repeat = True

while repeat:
    value = print_option()
    result = calc(value[1], float(value[0]), float(value[2]))
    print(result)
    
    repeat = input('Sair [S/N]: ').upper() == 'N'
