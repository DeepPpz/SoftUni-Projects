def logged(function):
    def decorator(*args):
        result = function(*args)
        return f"you called {function.__name__}{args}\nit returned {result}"
    return decorator


@logged
def func(*args):
    return 3 + len(args)

print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b

print(sum_func(1, 4))
