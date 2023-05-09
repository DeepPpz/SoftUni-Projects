def check_null_values(value, default):
    if value == "null":
        value = default
    return value


DAMAGE_DEF, HEALTH_DEF, ARMOR_DEF = 45, 250, 10
dragon_army = {}
n = int(input())

for i in range(n):
    type_dragon, name, dmg, hp, armor = map(str, input().split())

    dmg = check_null_values(dmg, DAMAGE_DEF)
    hp = check_null_values(hp, HEALTH_DEF)
    armor = check_null_values(armor, ARMOR_DEF)

    if type_dragon not in dragon_army:
        dragon_army[type_dragon] = {name: {'damage': int(dmg), 'health': int(hp), 'armor': int(armor)}}
    elif name not in dragon_army[type_dragon]:
        dragon_army[type_dragon][name] = {'damage': int(dmg), 'health': int(hp), 'armor': int(armor)}
    else:
        dragon_army[type_dragon][name]['damage'] = int(dmg)
        dragon_army[type_dragon][name]['health'] = int(hp)
        dragon_army[type_dragon][name]['armor'] = int(armor)

for type_dragon in dragon_army:
    dragon_army[type_dragon] = dict(sorted(dragon_army[type_dragon].items(), key=lambda x: x[0]))

for type_dragon in dragon_army:
    dmg, hp, armor = 0, 0, 0
    for name in dragon_army[type_dragon]:
        dmg += dragon_army[type_dragon][name]['damage']
        hp += dragon_army[type_dragon][name]['health']
        armor += dragon_army[type_dragon][name]['armor']

    total_dragons = len(dragon_army[type_dragon])
    print(f"{type_dragon}::", end='')
    print(f"({dmg/total_dragons:.2f}/{hp/total_dragons:.2f}/{armor/total_dragons:.2f})")

    for (name, stats) in dragon_army[type_dragon].items():
        print(f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}")
