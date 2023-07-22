def integer_to_base(number, to_base):
    new_base = ''
    while number > 0:
        number, rem = divmod(number, to_base)
        new_base = str(rem) + new_base
    return new_base


num = int(input())
base = int(input())

print(integer_to_base(num, base))
