num = int(input())
first_num = num // 100
second_num = (num % 100) // 10
third_num = num % 10
n = first_num + second_num
m = first_num + third_num

for row in range(n):
    for col in range(m):
        if num % 5 == 0:
            num -= first_num
        elif num % 3 == 0:
            num -= second_num
        else:
            num += third_num
        print(num, end=' ')
    print()
