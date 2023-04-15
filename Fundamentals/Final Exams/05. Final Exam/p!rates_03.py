cities = {}

line = input().split("||")

while line[0] != "Sail":
    town, population, gold = line[0], int(line[1]), int(line[2])

    if town not in cities:
        cities[town] = {"population": population, "gold": gold}
    else:
        cities[town]["population"] += population
        cities[town]["gold"] += gold

    line = input().split("||")

while True:
    command = input().split("=>")
    action = command[0]

    if action == "End":
        break

    if action == "Plunder":
        town, people, gold = command[1], int(command[2]), int(command[3])
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")

        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            print(f"{town} has been wiped off the map!")
            del cities[town]

    elif action == "Prosper":
        town, gold = command[1], int(command[2])

        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town]["gold"] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {cities[town]['gold']} gold.")

if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for town in cities.keys():
        print(f"{town} -> Population: {cities[town]['population']} citizens, Gold: {cities[town]['gold']} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
