import re

while True:
    data = input()

    if data:
        numbers = re.findall(r"\d+", data)
        if numbers:
            print(*numbers, sep=" ", end=" ")
    else:
        exit()
