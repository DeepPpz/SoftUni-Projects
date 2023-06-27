money = input().split(', ')
beggars = int(input())

total_sum = []

for _ in range(beggars):
    total_sum.append(int(0))

while len(money) > 0:
    for i in range(beggars):
        total_sum[i] += int(money[i])
        if i == (len(money) - 1):
            break

    del money[0:i + 1]

print(total_sum)
