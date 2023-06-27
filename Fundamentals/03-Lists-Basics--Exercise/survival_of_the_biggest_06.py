orig_line = input().split()
n = int(input())

orig_line = list(map(int, orig_line))

for _ in range(n):
    min_num = min(orig_line)
    orig_line.remove(min_num)

print(*orig_line, sep=', ')
