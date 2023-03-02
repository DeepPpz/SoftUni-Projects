total_floors = int(input())
rooms_floor = int(input())

type_floor = ""

for floor in range(total_floors, 0, - 1):
    for room in range(rooms_floor):
        if floor == total_floors:
            type_floor = "L"
        elif floor % 2 == 0:
            type_floor = "O"
        else:
            type_floor = "A"
        print(f'{type_floor}{floor}{room}', end = " ")
    print()