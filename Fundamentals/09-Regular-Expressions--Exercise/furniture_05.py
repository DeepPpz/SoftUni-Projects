import re

pattern = re.compile(r"^>>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quant>\d+)$")
total_cost = 0
furniture = []

while True:
    data = input()

    if data == "Purchase":
        print("Bought furniture:")
        if len(furniture) > 0:
            print(*furniture, sep="\n")
        print(f"Total money spend: {total_cost:.2f}")
        exit()

    curr_furniture = re.search(pattern, data)

    if curr_furniture:
        furniture.append(curr_furniture.group("name"))
        total_cost += float(curr_furniture.group("price")) * float(curr_furniture.group("quant"))
