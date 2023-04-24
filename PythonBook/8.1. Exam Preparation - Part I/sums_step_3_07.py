n = int(input())
sum1 = sum2 = sum3 = 0

for i in range(n):
    num = int(input())

    if i % 3 == 0:
        sum1 += num
    elif i % 3 == 1:
        sum2 += num
    elif i % 3 == 2:
        sum3 += num

print(f"sum1 = {sum1}")
print(f"sum2 = {sum2}")
print(f"sum3 = {sum3}")
