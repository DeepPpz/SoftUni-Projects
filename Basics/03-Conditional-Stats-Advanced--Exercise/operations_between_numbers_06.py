n1 = int(input())
n2 = int(input())
operator = input()

result = 0
text = str

if operator == '+':
    result = n1 + n2
    if result % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {text}')

elif operator == '-':
    result = n1 - n2
    if result % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {text}')

elif operator == '*':
    result = n1 * n2
    if result % 2 == 0:
        text = 'even'
    else:
        text = 'odd'
    print(f'{n1} {operator} {n2} = {result} - {text}')

elif operator == '/':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 / n2
        print(f'{n1} / {n2} = {result:.2f}')

elif operator == '%':
    if n2 == 0:
        print(f'Cannot divide {n1} by zero')
    else:
        result = n1 % n2
        print(f'{n1} % {n2} = {result}')
