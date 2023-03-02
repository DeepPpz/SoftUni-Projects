n1 = int(input())
n2 = int(input())
operator = input()

result, type_num, output = 0, '', ''

if n2 == 0 and operator in ['/', '%']:
    output = f'Cannot divide {n1} by zero'

elif operator == '/':
    result = n1 / n2
    output = f"{n1} / {n2} = {result:.2f}"
elif operator == '%':
    result = n1 % n2
    output = f"{n1} % {n2} = {result}"
else:
    if operator == '+':
        result = n1 + n2
    elif operator == '-':
        result = n1 - n2
    elif operator == '*':
        result = n1 * n2

    if result % 2 == 0:
        type_num = 'even'
    else:
        type_num = 'odd'

    output = f"{n1} {operator} {n2} = {result} - {type_num}"

print(output)