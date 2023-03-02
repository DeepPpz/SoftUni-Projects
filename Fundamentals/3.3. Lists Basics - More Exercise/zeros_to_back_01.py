numbers = input().split(', ')

numbers = list(map(int, numbers))
new_list = []
zeros = 0

for i in range(len(numbers)):
    if numbers[i] == 0:
        zeros += 1
    else:
        new_list.append(numbers[i])

for i in range(zeros):
    new_list.append(0)

print(new_list)