text = input().lower()

vowels_sum = 0

for let in text:
    if let == 'a':
        vowels_sum += 1
    elif let == 'e':
        vowels_sum += 2
    elif let == 'i':
        vowels_sum += 3
    elif let == 'o':
        vowels_sum += 4
    elif let == 'u':
        vowels_sum += 5

print(f'{vowels_sum}')