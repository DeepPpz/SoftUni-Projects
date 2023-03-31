import re
pairs_pattern = r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
mirrors = {}

text = input()
pairs = re.findall(pairs_pattern, text)
total_pairs = len(pairs)

for p in pairs:
    first_word, second_word = map(str, (p[1], p[2]))

    if first_word[::-1] == second_word:
        mirrors[first_word] = second_word

if total_pairs == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{total_pairs} word pairs found!")
    if not mirrors:
        print("No mirror words!")
    else:
        print(f"The mirror words are:")
        counter = 0
        for (f, s) in mirrors.items():
            counter += 1
            if counter < len(mirrors):
                print(f"{f} <=> {s}", end=", ")
            else:
                print(f"{f} <=> {s}")
