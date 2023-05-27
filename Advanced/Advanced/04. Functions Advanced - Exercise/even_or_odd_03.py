def even_odd(*args):
    command = args[-1]
    numbers = list(args[:-1])

    if command == "even":
        return [x for x in numbers if x % 2 == 0]
    elif command == "odd":
        return [x for x in numbers if x % 2 != 0]
