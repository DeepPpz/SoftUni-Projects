start_letter = input()
end_letter = input()
miss_letter = input()

combination_count = 0

start_letter = ord(start_letter)
end_letter = ord(end_letter)
miss_letter = ord(miss_letter)

for x1 in range(start_letter, end_letter + 1):
    if x1 == miss_letter:
        continue
    for x2 in range(start_letter, end_letter + 1):
        if x2 == miss_letter:
            continue
        for x3 in range(start_letter, end_letter + 1):
            if x3 == miss_letter:
                continue
            else:
                combination_count += 1
                print(f'{chr(x1)}{chr(x2)}{chr(x3)}', end= ' ')

print(f'{combination_count}')