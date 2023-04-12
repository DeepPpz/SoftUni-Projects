n = int(input())

cols = 2 * n - 1

for i in range(n):
    dots = (cols - n) // 2
    mid = cols - (2 * dots + 2)

    if i == 0:
        print("." * dots + "#" * n + "." * dots)
    elif i == n - 1:
        print("#" * (dots + 1) + "." * mid + "#" * (dots + 1))
    else:
        print("." * dots + "#" + "." * mid + "#" + "." * dots)

for i in range(1, n):
    dots = i
    mid = cols - (2 * dots + 2)

    if i == n - 1:
        print("." * dots + "#" + "." * dots)
    else:
        print("." * dots + "#" + "." * mid + "#" + "." * dots)
