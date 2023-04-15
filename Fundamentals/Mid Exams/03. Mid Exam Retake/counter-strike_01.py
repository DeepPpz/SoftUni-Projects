energy = int(input())
won_battles = 0

while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {won_battles}. Energy left: {energy}")
        exit()

    distance = int(distance)

    if energy >= distance:
        won_battles += 1
        energy -= distance
    else:
        print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
        exit()

    if won_battles % 3 == 0:
        energy += won_battles
