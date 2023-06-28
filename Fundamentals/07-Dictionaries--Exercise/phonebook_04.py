phonebook = {}
data = input().split("-")

while data[0].isdigit() is False:
    phonebook[data[0]] = data[1]
    data = input().split("-")

n = int(data[0])

for i in range(n):
    name = input()

    if name in phonebook:
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f"Contact {name} does not exist.")
