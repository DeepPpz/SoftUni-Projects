def make_bold(function):
    def decorator(*args):
        text = function(*args)
        return f"<b>{text}</b>"
    return decorator


def make_italic(function):
    def decorator(*args):
        text = function(*args)
        return f"<i>{text}</i>"
    return decorator


def make_underline(function):
    def decorator(*args):
        text = function(*args)
        return f"<u>{text}</u>"
    return decorator


@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
