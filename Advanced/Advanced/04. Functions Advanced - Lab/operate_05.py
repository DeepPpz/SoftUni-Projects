from functools import reduce


def operate(operator, *numbers):
    if operator == "+":
        return reduce(lambda a, b: a+b, numbers)
    elif operator == "-":
        return reduce(lambda a, b: a-b, numbers)
    elif operator == "*":
        return reduce(lambda a, b: a*b, numbers)
    elif operator == "/":
        return reduce(lambda a, b: a/b, numbers)
