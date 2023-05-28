from collections import deque

string = deque(input().split())
colors_found = []
all_colors = ("red", "yellow", "blue", "orange", "purple", "green")
color_maker = {
    "orange": ("red", "yellow"),
    "purple": ("red", "blue"),
    "green": ("yellow", "blue")
}

while len(string):
    second_str = string.pop() if len(string) > 1 else ""
    first_str = string.popleft()

    if (first_str + second_str) in all_colors:
        colors_found.append(first_str + second_str)
    elif (second_str + first_str) in all_colors:
        colors_found.append(second_str + first_str)
    else:
        if first_str[:- 1]:
            string.insert(len(string) // 2, first_str[:- 1])
        if second_str[:- 1]:
            string.insert(len(string) // 2, second_str[:- 1])

for color in colors_found:
    if color in color_maker:
        if color_maker[color][0] not in colors_found or color_maker[color][1] not in colors_found:
            colors_found.remove(color)

print(colors_found)
