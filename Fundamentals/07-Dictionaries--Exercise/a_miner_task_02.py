resources = {}
curr_resource = input()

while curr_resource != "stop":
    quantity = int(input())

    if curr_resource not in resources:
        resources[curr_resource] = quantity
    else:
        resources[curr_resource] += quantity

    curr_resource = input()

for (key, value) in resources.items():
    print(f"{key} -> {value}")
