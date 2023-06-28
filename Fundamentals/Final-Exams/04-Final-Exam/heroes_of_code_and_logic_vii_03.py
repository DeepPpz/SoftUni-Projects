n = int(input())
heroes = {}
MAX_HP, MAX_MP = 100, 200

for _ in range(n):
    hero, hp, mp = map(str, input().split())
    heroes[hero] = {"hp": int(hp), "mp": int(mp)}

while True:
    line = input().split(" - ")
    command = line[0]

    if command == "End":
        break

    if command == "CastSpell":
        hero, mp, spell = line[1], int(line[2]), line[3]

        if mp <= heroes[hero]["mp"]:
            heroes[hero]["mp"] -= mp
            print(f"{hero} has successfully cast {spell} and now has {heroes[hero]['mp']} MP!")
        else:
            print(f"{hero} does not have enough MP to cast {spell}!")

    elif command == "TakeDamage":
        hero, damage, attacker = line[1], int(line[2]), line[3]
        heroes[hero]["hp"] -= damage

        if heroes[hero]["hp"] > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {heroes[hero]['hp']} HP left!")
        else:
            del heroes[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif command == "Recharge":
        hero, mp = line[1], int(line[2])
        curr_mp = heroes[hero]["mp"]

        if curr_mp + mp > MAX_MP:
            mp = MAX_MP - curr_mp
            heroes[hero]["mp"] = MAX_MP
        else:
            heroes[hero]["mp"] += mp
        print(f"{hero} recharged for {mp} MP!")

    elif command == "Heal":
        hero, hp = line[1], int(line[2])
        curr_hp = heroes[hero]["hp"]

        if curr_hp + hp > MAX_HP:
            hp = MAX_HP - curr_hp
            heroes[hero]["hp"] = MAX_HP
        else:
            heroes[hero]["hp"] += hp
        print(f"{hero} healed for {hp} HP!")

for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['hp']}\n  MP: {heroes[hero]['mp']}")
