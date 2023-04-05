import re
pattern = re.compile(r"(?P<boss>\|[A-Z]{4,}\|):(?P<title>#[A-Za-z]+\s[A-Za-z]+#)")

n = int(input())

for _ in range(n):
    curr_person = input()

    valid_boss = re.search(pattern, curr_person)

    if valid_boss:
        boss = valid_boss.group("boss").strip("|")
        title = valid_boss.group("title").strip("#")
        print(f"{boss}, The {title}")
        print(f">> Strength: {len(boss)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
