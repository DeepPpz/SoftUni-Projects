curr_string = input()

forbidden_vowels = ['a', 'o', 'u', 'e', 'i']
new_string = [curr_string[i] for i in range(len(curr_string)) if curr_string[i].lower() not in forbidden_vowels]

print(''.join(new_string))