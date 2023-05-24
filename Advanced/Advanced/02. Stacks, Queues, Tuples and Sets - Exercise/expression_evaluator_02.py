from collections import deque
import math

string_expression = input().split()
expression = deque()
final_result = 0
arithmetic_operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: math.floor(x / y)
}

for sym in string_expression:
    if sym in "+-*/":
        while len(expression) > 1:
            expression.appendleft(arithmetic_operations[sym](expression.popleft(), expression.popleft()))
    else:
        expression.append(int(sym))

print(expression.popleft())
