inventory = input().split(", ")

while True:
    command = input().split(" - ")
    action = command[0]

    if action == "Craft!":
        print(*inventory, sep=', ')
        exit(0)

    item = command[1]

    if action == "Collect":
        if item not in inventory:
            inventory.append(item)

    elif action == "Drop":
        try:
            inventory.remove(item)
        except ValueError:
            pass

    elif action == "Combine Items":
        old_item, new_item = map(str, item.split(":"))
        try:
            idx = inventory.index(old_item) + 1
            inventory.insert(idx, new_item)
        except ValueError:
            pass

    elif action == "Renew":
        try:
            inventory.remove(item)
            inventory.append(item)
        except ValueError:
            pass
