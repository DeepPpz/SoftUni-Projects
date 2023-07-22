n = int(input())

min_num = 10000000000000000000

for i in range(n):
    number = int(input())
    if number < min_num:
        min_num = number

print(min_num)