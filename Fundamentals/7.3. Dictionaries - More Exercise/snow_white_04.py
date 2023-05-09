dwarves_data = {}
end_result = []

while True:
    command = input().split(" <:> ")
    if command[0] == "Once upon a time":
        break

    dwarf, color, physics = command[0], command[1], int(command[2])

    if color not in dwarves_data:
        dwarves_data[color] = {dwarf: physics}
    elif dwarf not in dwarves_data[color]:
        dwarves_data[color][dwarf] = physics
    else:
        curr_physics = dwarves_data[color][dwarf]
        dwarves_data[color][dwarf] = max(curr_physics, physics)

for color in dwarves_data:
    for dwarf, physic in dwarves_data[color].items():
        end_result.append({"color_len": len(dwarves_data[color]), "name": dwarf, "physics": physic, "color": color})
for show in sorted(end_result, key=lambda item: (-item["physics"], -item["color_len"])):
    print(f"({show['color']}) {show['name']} <-> {show['physics']}")
