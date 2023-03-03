def check_materials(d):
    if any(v >= 250 for v in d.values()):
        return True
    return False


def obtained_item(d):
    if d["shards"] >= 250:
        d["shards"] -= 250
        print("Shadowmourne obtained!")
    elif d["fragments"] >= 250:
        d["fragments"] -= 250
        print("Valanyr obtained!")
    elif d["motes"] >= 250:
        d["motes"] -= 250
        print("Dragonwrath obtained!")


key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}

while True:
    data = input().lower().split(" ")

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i+1]

        if material in key_materials:
            key_materials[material] += quantity
        elif material in junk_materials:
            junk_materials[material] += quantity
        else:
            junk_materials[material] = quantity

        if check_materials(key_materials):
            obtained_item(key_materials)

            for (key, value) in key_materials.items():
                print(f"{key}: {value}")
            for (key, value) in junk_materials.items():
                print(f"{key}: {value}")
            exit()
