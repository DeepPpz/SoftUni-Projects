import re
place_pattern = r"(=|/)([A-Z][A-Za-z]{2,})\1"

data = input()

places = [p[1] for p in re.findall(place_pattern, data)]
travel_points = sum([len(x) for x in places])

print("Destinations: ", end='')
print(*places, sep=", ")
print(f"Travel Points: {travel_points}")
