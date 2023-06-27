import re

first_word = input()
second_word = input()

old_word, new_word = '', ''
prints = []

for i in range(len(first_word)):
    old_word += first_word[i]
    for j in range(i + 1):
        if i != j:
            continue

        new_word += second_word[j]

        if old_word != new_word:
            diff = re.sub(old_word, new_word, first_word, i + 1)
            if diff not in prints:
                print(diff)
                prints.append(diff)
            if diff == second_word:
                exit()
