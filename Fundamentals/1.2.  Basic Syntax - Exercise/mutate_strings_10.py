import re

first_word = input()
second_word = input()

old_word, new_word = '', ''
prints = []

for i1 in range(len(first_word)):
    old_word += first_word[i1]
    for i2 in range(i1+1):
        if i1 != i2:
            continue

        new_word += second_word[i2]

        if old_word != new_word:
            diff = re.sub(old_word, new_word, first_word, i1+1)
            if diff not in prints:
                print(diff)
                prints.append(diff)
            if diff == second_word:
                exit()