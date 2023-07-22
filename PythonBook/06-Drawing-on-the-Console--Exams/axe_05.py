n = int(input())

cols = 5 * n
begin = 3 * n
mid, end = 0, 0

for i in range(n):
    mid = i
    end = cols - mid - begin - 2
    print("-" * begin + "*" + "-" * mid + "*" + "-" * end)

axe_handle = n // 2

for i in range(axe_handle):
    print("*" * begin + "*" + "-" * mid + "*" + "-" * end)

for i in range(axe_handle - 1):
    print("-" * begin + "*" + "-" * mid + "*" + "-" * end)
    begin -= 1
    end -= 1
    mid += 2

print("-" * begin + "*" + "*" * mid + "*" + "-" * end)
