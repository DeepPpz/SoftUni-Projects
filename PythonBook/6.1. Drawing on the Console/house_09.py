n = int(input())

if n % 2 == 0:
    m = n // 2
    stars = 2
    hyphens = (n - 2) // 2
else:
    m = n // 2 + 1
    stars = 1
    hyphens = (n - 1) // 2

line = "-" * hyphens + "*" * stars + "-" * hyphens
print(line)

for i in range(1, m):
    stars += 2
    hyphens -= 1
    line = "-" * hyphens + "*" * stars + "-" * hyphens
    print(line)

for i in range(n // 2):
    line = "|" + "*" * (n - 2) + "|"
    print(line)
