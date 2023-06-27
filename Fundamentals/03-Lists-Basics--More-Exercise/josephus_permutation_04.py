people = input().split()
k = int(input())

temp_idx, kill_order = [], []
idx_counter = 0

while len(people) > 0:
    for i in range(len(people)):
        idx_counter += 1
        if idx_counter % k == 0:
            kill_order.append(people[i])
            temp_idx.append(i)

    temp_idx.reverse()

    for i in range(len(people) - 1, - 1, - 1):
        if i in temp_idx:
            people.pop(i)
    temp_idx.clear()

result = ','.join(kill_order)
print(f'[{result}]')
