text = input()

total = 0

for letter in text:
    if letter == 'a': total += 1
    elif letter == 'e': total += 2
    elif letter == 'i': total += 3
    elif letter == 'o': total += 4
    elif letter == 'u': total += 5

print(total)