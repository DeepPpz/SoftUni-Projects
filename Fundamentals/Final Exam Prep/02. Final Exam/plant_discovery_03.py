n = int(input())
exhibition = {}

for _ in range(n):
    plant, rarity = map(str, input().split("<->"))

    if plant in exhibition:
        exhibition[plant]["rarity"] = int(rarity)
    else:
        exhibition[plant] = {"rarity": int(rarity), "rating": []}

while True:
    command = input().split(": ")

    if command[0] == "Exhibition":
        break

    if command[0] == "Rate":
        plant, rating = map(str, command[1].split(" - "))
        if plant not in exhibition:
            print("error")
        else:
            exhibition[plant]["rating"].append(int(rating))

    elif command[0] == "Update":
        plant, rarity = map(str, command[1].split(" - "))
        if plant not in exhibition:
            print("error")
        else:
            exhibition[plant]["rarity"] = rarity

    elif command[0] == "Reset":
        plant = command[1]
        if plant not in exhibition:
            print("error")
        else:
            exhibition[plant]["rating"].clear()

print("Plants for the exhibition:")
for plant in exhibition:
    if len(exhibition[plant]["rating"])!= 0:
        avg_rating = sum(exhibition[plant]["rating"]) / len(exhibition[plant]["rating"])
    else:
        avg_rating = 0
    print(f"- {plant}; Rarity: {exhibition[plant]['rarity']}; Rating: {avg_rating:.2f}")
