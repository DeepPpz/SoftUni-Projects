secret_message = input().split()

for i in range(len(secret_message)):
    curr_string = [el for el in secret_message[i]]
    temp_str = ''
    for el in secret_message[i]:
        if el.isdigit():
            temp_str += el
        else:
            break

    curr_string = list(filter(lambda x: not x.isdigit(), curr_string))
    curr_string.insert(0, chr(int(temp_str)))
    curr_string[1], curr_string[-1] = curr_string[-1], curr_string[1]
    secret_message[i] = ''.join(curr_string)

print(*secret_message, sep=' ')