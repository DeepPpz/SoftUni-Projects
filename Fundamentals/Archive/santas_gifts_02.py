n = int(input())
neighborhood = input().split()
curr_position = 0

for i in range(n):
    line = input().split()
    action = line[0]

    if action == "Forward":
        steps = int(line[1])

        if curr_position + steps < len(neighborhood):
            curr_position += steps
            neighborhood.pop(curr_position)

    elif action == "Back":
        steps = int(line[1])

        if curr_position - steps >= 0:
            curr_position -= steps
            neighborhood.pop(curr_position)

    elif action == "Gift":
        idx, house = int(line[1]), line[2]

        if 0 <= idx <= len(neighborhood):
            neighborhood.insert(idx, house)
            curr_position = idx

    elif action == "Swap":
        house_one, house_two = line[1], line[2]
        if house_one in neighborhood and house_two in neighborhood:
            idx_one = neighborhood.index(house_one)
            idx_two = neighborhood.index(house_two)
            neighborhood[idx_one], neighborhood[idx_two] = neighborhood[idx_two], neighborhood[idx_one]

print(f"Position: {curr_position}")
print(*neighborhood, sep=', ')
