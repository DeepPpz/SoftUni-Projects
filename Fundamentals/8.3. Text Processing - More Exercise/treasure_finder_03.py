key = [int(x) for x in input().split()]

while True:
    line = input()
    counter, treasure, symbols = 0, "", []

    if line == 'find':
        break

    for i in range(len(line)):
        curr_el = ord(line[i]) - key[counter]
        curr_el = chr(curr_el)
        treasure += curr_el

        if curr_el in ["&", "<", ">"]:
            symbols.append(i)

        counter += 1
        if counter == len(key):
            counter = 0

    type_treasure = treasure[symbols[0] + 1: symbols[1]]
    coordinates = treasure[symbols[2] + 1: symbols[3]]

    print(f"Found {type_treasure} at {coordinates}")
