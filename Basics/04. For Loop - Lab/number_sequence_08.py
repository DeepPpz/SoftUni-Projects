count = int(input())

max_number = -100000000000000000000000000000
min_number = 100000000000000000000000000000

for check in range(count):
    number = int(input())
    if number > max_number: max_number = number
    if number < min_number: min_number = number

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')