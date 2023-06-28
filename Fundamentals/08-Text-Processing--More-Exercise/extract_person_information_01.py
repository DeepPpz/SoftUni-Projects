n = int(input())

for _ in range(n):
    text = input()

    x = text.find("@")
    y = text.find("|")
    name = text[x + 1:y]

    x = text.find("#")
    y = text.find("*")
    age = text[x + 1:y]

    print(f"{name} is {age} years old.")
