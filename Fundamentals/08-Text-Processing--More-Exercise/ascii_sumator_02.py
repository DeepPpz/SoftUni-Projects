start = ord(input())
end = ord(input())
random_string = [ord(x) for x in input()]

total_sum = 0

for el in random_string:
    if start < el < end:
        total_sum += el

print(total_sum)
