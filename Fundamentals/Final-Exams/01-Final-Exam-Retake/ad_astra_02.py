import re
pattern = r"(#|\|)(?P<item>[A-Za-z]+(\s?[A-Za-z])*)\1(?P<date>\d{2}(/\d{2}){2})\1(?P<cal>\d+)\1"
DAILY_CALORIES = 2000

data = input()

total_calories = sum([int(f.group("cal")) for f in re.finditer(pattern, data)])
food = re.finditer(pattern, data)

print(f"You have food to last you for: {total_calories // DAILY_CALORIES} days!")
for f in food:
    print(f"Item: {f.group('item')}, Best before: {f.group('date')}, Nutrition: {f.group('cal')}")
