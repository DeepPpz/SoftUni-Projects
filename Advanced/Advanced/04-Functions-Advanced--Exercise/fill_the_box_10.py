def fill_the_box(height, length, width, *commands):
    box_size = height * length * width
    free_space = box_size
    finish_idx = commands.index("Finish")
    commands = commands[:finish_idx]

    for i in range(len(commands)):
        cubes = commands[i]
        if free_space - cubes > 0:
            free_space -= cubes
        else:
            cubes_left = cubes - free_space + sum(commands[i + 1:])
            return f"No more free space! You have {cubes_left} more cubes."

    if free_space:
        return f"There is free space in the box. You could put {free_space} more cubes."
