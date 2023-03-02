def calculate(operators, num_one, num_two):
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


operator = input()
num_one = int(input())
num_two = int(input())

print(calculate(operator, num_one, num_two))