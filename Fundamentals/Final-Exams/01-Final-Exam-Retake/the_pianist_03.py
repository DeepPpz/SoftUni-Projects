n = int(input())
works = {}

for i in range(n):
    line = input().split("|")
    works[line[0]] = {"composer": line[1], "key": line[2]}

while True:
    command = input().split("|")
    action = command[0]

    if action == 'Stop':
        for piece in works.keys():
            print(f"{piece} -> Composer: {works[piece]['composer']}, Key: {works[piece]['key']}")
        exit()

    if action == 'Add':
        piece, composer, key = command[1], command[2], command[3]
        if piece in works:
            print(f"{piece} is already in the collection!")
        else:
            works[piece] = {"composer": composer, "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        piece = command[1]
        if piece in works:
            del works[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece, key = command[1], command[2]
        if piece in works:
            works[piece]["key"] = key
            print(f"Changed the key of {piece} to {key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
