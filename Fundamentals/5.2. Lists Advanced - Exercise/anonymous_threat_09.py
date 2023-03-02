def merging_strings(i, j):
    if i < 0:
        i = 0
    if j > len(text) - 1:
        j = len(text) - 1
    temp_list = text[:i]
    temp_list.append(''.join(text[i:j + 1]))
    temp_list.extend(text[j + 1:])
    return temp_list


def dividing_strings(idx, part):
    temp_text = [el for el in text[idx]]
    text.pop(idx)
    divided_list = []
    n = len(temp_text) // part

    for l in range(part - 1):
        divided_list.append(''.join(temp_text[:n]))
        temp_text = temp_text[n:]
    divided_list.append(''.join(temp_text))
    temp_list = text[:idx] + divided_list + text[idx:]
    return temp_list


text = input().split()
command = input().split()

while command[0] != '3:1':
    num_one, num_two = map(int, (command[1], command[2]))

    if command[0] == 'merge':
        text = merging_strings(num_one, num_two)
    elif command[0] == 'divide':
        text = dividing_strings(num_one, num_two)

    command = input().split()

print(' '.join(text))
