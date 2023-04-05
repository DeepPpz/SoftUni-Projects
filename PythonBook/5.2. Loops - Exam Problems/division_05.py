n = int(input())
p1, p2, p3 = 0, 0, 0

for i in range(n):
    curr_num = int(input())

    if curr_num % 2 == 0:
        p1 += 1

    if curr_num % 3 == 0:
        p2 += 1

    if curr_num % 4 == 0:
        p3 += 1

print(f"{(p1 / n * 100):.2f}%")
print(f"{(p2 / n * 100):.2f}%")
print(f"{(p3 / n * 100):.2f}%")
