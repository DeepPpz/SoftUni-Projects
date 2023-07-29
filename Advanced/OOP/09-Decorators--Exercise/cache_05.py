def cache(func):
    def decorator(num):
        if num not in decorator.log:
            decorator.log[num] = func(num)
        return decorator.log[num]
    
    decorator.log = {}
    return decorator


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


fibonacci(3)
print(fibonacci.log)

fibonacci(4)
print(fibonacci.log)
