numbers = input().split()
reversed_numbers = []

for _ in range(len(numbers)):
    reversed_numbers.append(numbers.pop())

print(*reversed_numbers, sep=' ')
