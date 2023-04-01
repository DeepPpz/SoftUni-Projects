import re
pattern = re.compile(r"(?P<planet>@[A-Za-z]+)[^@,!:>-]*(?P<popul>:\d+)[^@,!:>-]*"
                     r"(?P<type>![AD]!)[^@,!:>-]*(?P<soldier>->\d+)")
n = int(input())
attacked, destroyed = [], []

for i in range(n):
    message = input()
    decryption_key = sum(1 for x in message if x in ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R'])
    message = ''.join([chr(ord(x) - decryption_key) for x in message])

    valid_planet = re.search(pattern, message)

    if valid_planet:
        planet = valid_planet.group("planet").lstrip("@")
        attack_type = valid_planet.group("type").strip("!")
        if attack_type == "A":
            attacked.append(planet)
        else:
            destroyed.append(planet)

attacked = sorted(attacked)
destroyed = sorted(destroyed)

print(f"Attacked planets: {len(attacked)}")
for a in attacked:
    print(f"-> {a}")
print(f"Destroyed planets: {len(destroyed)}")
for d in destroyed:
    print(f"-> {d}")
