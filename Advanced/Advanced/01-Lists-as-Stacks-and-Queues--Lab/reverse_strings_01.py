curr_string = list(input())
reversed_string = []

for i in range(len(curr_string)):
    reversed_string.append(curr_string.pop())

print(*reversed_string, sep='')
