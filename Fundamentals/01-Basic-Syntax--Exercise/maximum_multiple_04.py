divisor = int(input())
boundary = int(input())
multiplicator = 0

for num in range(1, boundary + 1):
    if num % divisor == 0:
        multiplicator = num

print(multiplicator)
