from collections import deque

all_materials = deque([int(x) for x in input().split()])
all_magic_levels = deque([int(x) for x in input().split()])
presents = {}
needed_magic = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while all_materials and all_magic_levels:
    material = all_materials.pop()
    magic = all_magic_levels.popleft()

    if material == 0 and magic == 0:
        continue
    elif material == 0:
        all_magic_levels.appendleft(magic)
        continue
    elif magic == 0:
        all_materials.append(material)
        continue

    total_magic = material * magic
    if total_magic in needed_magic:
        present = needed_magic.get(total_magic)
        if present not in presents:
            presents[present] = 0
        presents[present] += 1
    elif total_magic < 0:
        all_materials.append(material + magic)
    else:
        all_materials.append(material + 15)

if ("Doll" in presents and "Train" in presents) or \
    ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if all_materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(all_materials)])}")
if all_magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in all_magic_levels])}")
for (toy, amount) in sorted(presents.items()):
    print(f"{toy}: {amount}")
