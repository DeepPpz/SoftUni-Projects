import re

data = input()

pattern = r"\b(?P<date>\d{2})(?P<sep>[-\.\/])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
dates = re.findall(pattern, data)

for d in dates:
    print(f"Day: {d[0]}, Month: {d[2]}, Year: {d[3]}")
