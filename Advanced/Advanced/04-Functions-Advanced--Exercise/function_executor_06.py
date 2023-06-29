def func_executor(*functions):
    result = ""
    for (func, args) in functions:
        nested_result = func(*args)
        result += f"{func.__name__} - {nested_result}\n"
    return result
