import re
health_pattern = re.compile(r"[^0-9+*,/.\-]")
damage_pattern = re.compile(r"[-+]?[0-9][.0-9]*")

participants = [x.strip() for x in input().split(',')]
demon_book = {}

for p in participants:
    health = sum([ord(x) for x in re.findall(health_pattern, p)])
    damage = sum([float(x) for x in re.findall(damage_pattern, p)])

    for s in p:
        if s == "*":
            damage *= 2
        elif s == "/":
            damage /= 2

    demon_book[p] = {"health": health, "damage": damage}

demon_book = dict(sorted(demon_book.items(), key=lambda x: x[0]))

for demon, demon_data in demon_book.items():
    print(f"{demon} - {demon_data['health']} health, {demon_data['damage']:.2f} damage")
