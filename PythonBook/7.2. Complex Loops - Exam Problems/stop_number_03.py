n = int(input())
m = int(input())
stop = int(input())

for i in range(m, n - 1, - 1):
    if i % 2 == 0 and i % 3 == 0:
        if i == stop:
            break
        print(i, end=' ')
