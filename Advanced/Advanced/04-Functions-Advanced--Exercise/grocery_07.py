def grocery_store(**inventory):
    sorted_inventory = dict(sorted(inventory.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    result = ""
    for (key, value) in sorted_inventory.items():
        result += f"{key}: {value}\n"
    return result
