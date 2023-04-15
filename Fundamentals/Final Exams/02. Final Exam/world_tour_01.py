def validate_index(index):
    if 0 <= index < len(stops):
        return True


stops = input()
command = input().split(":")

while command[0] != "Travel":
    if command[0] == "Add Stop":
        idx, string = int(command[1]), command[2]
        if validate_index(idx):
            stops = stops[:idx] + string + stops[idx:]

    elif command[0] == "Remove Stop":
        start_idx, end_idx = map(int, (command[1], command[2]))
        if validate_index(start_idx) and validate_index(end_idx):
            stops = stops[:start_idx] + stops[end_idx+1:]

    elif command[0] == "Switch":
        old_str, new_str = map(str, (command[1], command[2]))
        if old_str in stops:
            stops = stops.replace(old_str, new_str)

    print(stops)
    command = input().split(":")

print(f"Ready for world tour! Planned stops: {stops}")
