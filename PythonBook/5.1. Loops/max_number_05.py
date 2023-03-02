n = int(input())

max_num = -10000000000000000000

for i in range(n):
    number = int(input())
    if number > max_num:
        max_num = number

print(max_num)