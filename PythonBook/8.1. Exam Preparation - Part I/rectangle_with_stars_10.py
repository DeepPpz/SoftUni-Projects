n = int(input())

if n % 2 == 0:
    rows = n - 1
else:
    rows = n
ends = "%" * 2 * n

print(ends)
for r in range(rows):
    if r == rows // 2:
        spaces = (2 * n - 4) // 2
        print("%" + " " * spaces + "*" * 2 + " " * spaces + "%")
    else:
        spaces = 2 * n - 2
        print("%" + " " * spaces + "%")
print(ends)
