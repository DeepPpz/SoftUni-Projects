n = int(input())

for i in range(1, n + 1):
    print('*' * i)
for j in range(1, n + 1):
    print('*' * (n - j))
