groups_count = int(input())

total_people = 0
musala_people = 0
monblan_people = 0
kilim_people = 0
k2_people = 0
everest_people = 0

for groups in range(groups_count):
    people_count = int(input())
    total_people += people_count
    if people_count < 6: musala_people += people_count
    elif people_count < 13: monblan_people += people_count
    elif people_count < 26: kilim_people += people_count
    elif people_count < 41: k2_people += people_count
    else: everest_people += people_count

print(f'{musala_people / total_people * 100:.2f}%')
print(f'{monblan_people / total_people * 100:.2f}%')
print(f'{kilim_people / total_people * 100:.2f}%')
print(f'{k2_people / total_people * 100:.2f}%')
print(f'{everest_people / total_people * 100:.2f}%')