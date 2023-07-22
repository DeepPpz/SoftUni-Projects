def get_min(curr_min, new_value):
    if curr_min > new_value:
        return new_value
    else:
        return curr_min


values = [int(input()) for x in range(3)]
min_value = 10000000000000000000000

for i in range(len(values)):
    min_value = get_min(min_value, values[i])

print(min_value)
