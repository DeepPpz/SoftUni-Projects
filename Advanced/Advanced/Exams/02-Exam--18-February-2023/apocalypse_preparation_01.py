from collections import deque


all_textiles = deque([int(x) for x in input().split()])
all_medicaments = deque([int(x) for x in input().split()])
items_resources = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit'
}
crafted_items = {}

while all_textiles and all_medicaments:
    textile = all_textiles.popleft()
    medicament = all_medicaments.pop()
    resources = textile + medicament

    if resources in items_resources:
        item = items_resources[resources]
        if item not in crafted_items:
            crafted_items[item] = 0
        crafted_items[item] += 1
    elif resources > 100:
        if 'MedKit' not in crafted_items:
            crafted_items['MedKit'] = 0
        crafted_items['MedKit'] += 1

        all_medicaments.append((resources - 100) + all_medicaments.pop())

    else:
        all_medicaments.append(medicament + 10)

if not all_textiles and not all_medicaments:
    print('Textiles and medicaments are both empty.')
elif not all_textiles:
    print('Textiles are empty.')
elif not all_medicaments:
    print('Medicaments are empty.')

crafted_items = dict(sorted(crafted_items.items(), key=lambda x: (-x[1], x[0])))
[print(f'{key} - {value}') for (key, value) in crafted_items.items()]

if all_textiles:
    print(f'Textiles left: {", ".join(str(x) for x in all_textiles)}')
if all_medicaments:
    print(f'Medicaments left: {", ".join(str(x) for x in reversed(all_medicaments))}')
