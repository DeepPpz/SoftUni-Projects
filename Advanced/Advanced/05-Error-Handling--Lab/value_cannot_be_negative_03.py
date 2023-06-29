class ValueCannotBeNegativeError(Exception):
    """Raised when input value is negative"""
    pass


for i in range(5):
    num = int(input())

    if num < 0:
        raise ValueCannotBeNegativeError
