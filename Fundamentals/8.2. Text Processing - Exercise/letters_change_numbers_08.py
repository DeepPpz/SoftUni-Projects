from string import ascii_lowercase

sequences = input().split()
total_sum = 0
alphabet = [x for x in ascii_lowercase]

for s in sequences:
    before_letter, after_letter = s[0], s[len(s)-1]
    number = int(s[1:len(s)-1])
    position_before_letter = alphabet.index(before_letter.lower()) + 1
    position_after_letter = alphabet.index(after_letter.lower()) + 1

    if before_letter.isupper():
        curr_result = number / position_before_letter
    else:
        curr_result = number * position_before_letter

    if after_letter.isupper():
        curr_result -= position_after_letter
    else:
        curr_result += position_after_letter

    total_sum += curr_result

print(f"{total_sum:.2f}")
