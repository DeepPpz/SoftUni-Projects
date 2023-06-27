def calculate(operator, num_one, num_two):
    result = 0
    if operator == 'multiply':
        result = num_one * num_two
    elif operator == 'divide':
        result = num_one // num_two
    elif operator == 'add':
        result = num_one + num_two
    elif operator == 'subtract':
        result = num_one - num_two
    return result


operator_input = input()
num_one_input = int(input())
num_two_input = int(input())

print(calculate(operator_input, num_one_input, num_two_input))
