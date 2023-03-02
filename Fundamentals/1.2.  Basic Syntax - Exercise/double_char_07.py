
while True:
    current_string = input()

    if current_string == 'End':
        break
    elif current_string == 'SoftUni':
        continue
    else:
        new_string = ''

    for ch in current_string:
        new_string += ch * 2

    print(new_string)