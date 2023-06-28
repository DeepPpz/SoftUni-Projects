dungeon_rooms = input().split("|")
health = 100
bitcoins = 0

for i in range(len(dungeon_rooms)):
    action = dungeon_rooms[i].split()[0]
    amount = int(dungeon_rooms[i].split()[1])

    if action == "potion":
        healed = min((100 - health), amount)
        health = min(100, (health + amount))
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

    elif action == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        if health > amount:
            health -= amount
            print(f"You slayed {action}.")

        else:
            print(f"You died! Killed by {action}.")
            print(f"Best room: {i + 1}")
            exit(0)

print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")
