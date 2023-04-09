def calculate_fibonacci(num):
    """ Fibonacci sequences with recursive solution takes too much time!"""
    if num <= 1:
        return 1
    return calculate_fibonacci(num - 1) + calculate_fibonacci(num - 2)


def iterative_fibonacci(num):
    fib_0 = 1
    fib_1 = 1
    result = 0
    for _ in range(num - 1):
        result = fib_0 + fib_1
        fib_0, fib_1 = fib_1, result
    return result


num = int(input())

print(iterative_fibonnaci(num))
