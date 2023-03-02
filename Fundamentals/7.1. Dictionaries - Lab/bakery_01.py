data = input().split(" ")
inventory = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    inventory[key] = int(value)

print(inventory)