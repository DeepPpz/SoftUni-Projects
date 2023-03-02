def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a, b), c)


def subtract(sum, c):
    sub = sum_numbers(first_num, second_num) - third_num
    return sub


def sum_numbers(a, b):
    sum_num = first_num + second_num
    return sum_num


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))