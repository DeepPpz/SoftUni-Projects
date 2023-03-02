sequence = input().split()
key_string = input()

key_string = list(key_string)
message = ''

for i in range(len(sequence)):
    sequence[i] = list(map(int, sequence[i]))
    curr_idx = sum(sequence[i]) % len(key_string)

    message += key_string[curr_idx]
    key_string.pop(curr_idx)

print(message)