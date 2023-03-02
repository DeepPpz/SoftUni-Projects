data = input().split(" ")
inventory = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    inventory[key] = int(value)

checks = input().split()

for el in checks:
    if el in inventory:
        print(f"We have {inventory[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")