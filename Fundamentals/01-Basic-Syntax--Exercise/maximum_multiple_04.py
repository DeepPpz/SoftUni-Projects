divisor = int(input())
boundary = int(input())

for num in range(1, boundary + 1):
    if num % divisor == 0:
        multiplicator = num

print(multiplicator)
