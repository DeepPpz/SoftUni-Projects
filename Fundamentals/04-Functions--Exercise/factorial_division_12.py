def find_factorials(n):
    if n == 1:
        return 1
    else:
        return n * find_factorials(n - 1)


num_one = int(input())
num_two = int(input())

first_factorial = find_factorials(num_one)
second_factorial = find_factorials(num_two)
result = first_factorial / second_factorial

print(f'{result:.2f}')
