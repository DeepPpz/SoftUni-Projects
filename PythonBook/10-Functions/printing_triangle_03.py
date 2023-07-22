def print_line(start, end):
    for i in range(start, end + 1):
        print(i, end=" ")
    print()


n = int(input())

for idx in range(0, n + 1):
    print_line(1, idx)

for idx in range(n - 1, 0, -1):
    print_line(1, idx)
