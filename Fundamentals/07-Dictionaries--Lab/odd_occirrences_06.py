words = input().lower().split()

occurrences = {}

for el in words:
    if el not in occurrences:
        occurrences[el] = 1
    else:
        occurrences[el] += 1

for (key, value) in occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")
