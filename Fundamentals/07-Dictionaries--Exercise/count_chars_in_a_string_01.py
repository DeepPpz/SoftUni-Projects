string = list(input())
counter = {}

for el in string:
    if el == ' ':
        continue
    elif el not in counter:
        counter[el] = 1
    else:
        counter[el] += 1

for key, value in counter.items():
    print(f"{key} -> {value}")
