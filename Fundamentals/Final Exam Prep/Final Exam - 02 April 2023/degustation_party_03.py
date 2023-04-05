guests_preferences = {}
unliked_meals = 0

while True:
    command = input().split("-")

    if command[0] == "Stop":
        for guest in guests_preferences:
            print(f"{guest}: ", end="")
            print(*guests_preferences[guest], sep=", ")
        print(f"Unliked meals: {unliked_meals}")
        exit(0)

    action, guest, meal = map(str, command)

    if action == "Like":
        if guest not in guests_preferences:
            guests_preferences[guest] = [meal]
        elif meal not in guests_preferences[guest]:
            guests_preferences[guest].append(meal)

    elif action == "Dislike":
        if guest not in guests_preferences:
            print(f"{guest} is not at the party.")
        elif meal not in guests_preferences[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            guests_preferences[guest].remove(meal)
            unliked_meals += 1
            print(f"{guest} doesn't like the {meal}.")
