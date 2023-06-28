houses = [int(x) for x in input().split("@")]
position = 0

while True:
    command = input().split()

    if command[0] == "Love!":
        break

    steps = int(command[1])
    position = position + steps
    if position >= len(houses):
        position = 0

    if houses[position] == 0:
        print(f"Place {position} already had Valentine's day.")
        continue

    houses[position] -= 2
    if houses[position] == 0:
        print(f"Place {position} has Valentine's day.")

failed_houses = len(houses) - houses.count(0)
print(f"Cupid's last position was {position}.")
if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Mission was successful.")
