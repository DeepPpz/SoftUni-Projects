def define_type(a, b):
    if a == 'int':
        print(int(b) * 2)
    elif a == 'real':
        print(f'{int(b) * 1.5:.2f}')
    elif a == 'string':
        print(f'${b}$')


type_input = input()
input_value = input()

define_type(type_input, input_value)