import re

participants = input().split(", ")
pattern = r"[A-Za-z]|\d"
race = {p: 0 for p in participants}

while True:
    data = input()

    if data == "end of race":
        break

    matches = re.findall(pattern, data)
    name = ''.join(list(filter(lambda x: x.isalpha(), matches)))
    result = sum([int(x) for x in matches if x.isdigit()])

    if name in race:
        race[name] += result

ranked = sorted(race.items(), key=lambda x: -x[1])

print(f"1st place: {ranked[0][0]}")
print(f"2nd place: {ranked[1][0]}")
print(f"3rd place: {ranked[2][0]}")
